#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File       :   BaseGenTemplate.py
@License    :   (C)Copyright 2013-2023, capstone
@Project    :   play_with_python
@Software   :   PyCharm
@ModifyTime :   2023/2/35 20:39
@Author     :   liushuliang
@Version    :   1.0
@Description:   生成go/rust 模板
"""
import os
import sys

PYTHON_TARGET_DIR = 'F://play_with_code/play_with_python/problem/'
GO_TARGET_DIR = 'F://play_with_code/play_with_go/problem/'
RUST_TARGET_DIR = 'F://play_with_code/play_with_rust/src/problem/'


class BaseGenTemplate:
    def __init__(self, problem_url='https://atcoder.jp/contests/arc119/tasks/arc119_c'):
        self.url = problem_url
        self.site_tag = 'atc'

        parts = problem_url.split('/')
        self.contest = parts[-3]  # arc148
        self.task_id = parts[-1].split('_')[1] if '_' in parts[-1] else parts[-1][-1]  # c
        self.file_name = parts[-1]  # atc148_c
        self.spider = None

    def gen_rust_main_file(self, file):
        print(f'{file},创建成功')

        with open(file, 'w', encoding='utf-8') as f:
            print(f'创建模板文件{file}成功')
            f.write(f"""#[allow(unused)]
use std::collections::*;
use std::io::{{BufRead, BufWriter, Write}};

// const MOD:i64 = 1000000000+7;
#[allow(unused)]
pub fn solve(scan: &mut Scanner<impl BufRead>, out: &mut impl Write) {{
    let n = scan.token::<usize>();
    let mut a = vec![0i32; n];
    for i in 0..n {{
        a[i] = scan.token::<i32>();
    }}   
    let mut ans = 0;
    writeln!(out, "{{}}", ans).ok();
}}

pub fn run(scan: &mut Scanner<impl BufRead>, out: &mut impl Write) {{
    // let t = scan.token::<usize>();
    // for _ in 0..t {{
    //     solve(scan, out)
    // }}
    solve(scan,out)
}}

#[allow(unused)]
fn main() {{
    let sin = std::io::stdin();
    let scan = &mut Scanner::new(sin.lock());
    let sout = std::io::stdout();
    let out = &mut BufWriter::new(sout.lock());
    run(scan, out);
}}

pub struct Scanner<R> {{
    reader: R,
    buffer: Vec<String>,
}}
impl<R: ::std::io::BufRead> Scanner<R> {{
    pub fn new(reader: R) -> Self {{
        Self {{
            reader,
            buffer: vec![],
        }}
    }}
    pub fn token<T: ::std::str::FromStr>(&mut self) -> T {{
        loop {{
            if let Some(token) = self.buffer.pop() {{
                return token.parse().ok().expect("Failed parse");
            }}
            let mut input = String::new();
            self.reader.read_line(&mut input).expect("Failed read");
            self.buffer = input.split_whitespace().rev().map(String::from).collect();
        }}
    }}
    #[allow(unused)]
    pub fn token_bytes(&mut self) -> Vec<u8> {{
        let s = self.token::<String>();
        return s.as_bytes().into();
    }}
}}

// {self.url}
// 本模板由 https://github.com/liuliangcan/play_with_python/blob/main/tools/gen_code_tool/gen_template.py 自动生成;中文题面描述可移步
""")

    def gen_rust_test_file(self, file):
        """创建rust测试模板文件"""

        with open(file, 'w', encoding='utf-8') as f:
            print(f'创建测试文件{file}成功')
            cases = []
            for k, (_in, _out) in self.spider(self.url).cases().items():
                cases.append(f"""test_macro!({k},
                    b"{_in}",
                    "{_out}\n"
                );""")
            cases_str = '\n'.join(cases)
            f.write(f"""use super::{self.file_name}::Scanner;
use super::{self.file_name}::run;
#[cfg(test)]
mod {self.file_name} {{
    use super::*;

    macro_rules! test_macro {{
        ($name:ident, $input:expr, $expected:expr) => {{
            #[test]
            fn $name() {{
                let output = &mut Vec::new();
                let scan = &mut Scanner::new($input as &[u8]);
                run(scan, output);
                assert_eq!($expected, std::str::from_utf8(output).unwrap());
            }}
        }};
    }}

    {cases_str}
}}           
// {self.url}
// 本模板由 https://github.com/liuliangcan/play_with_python/blob/main/tools/gen_code_tool/gen_template.py 自动生成;中文题面描述可移步""")

    def make_go_paths(self):
        """创建go文件目录，并返回文件名"""
        files_path = os.path.join(GO_TARGET_DIR, self.site_tag, self.contest, self.task_id)
        if not os.path.exists(files_path):
            os.makedirs(files_path)
            main_file = os.path.join(files_path, f'{self.file_name}.go')
            test_file = os.path.join(files_path, f'{self.file_name}_test.go')
            return main_file, test_file
        else:
            sys.stderr.write(f'go: {files_path}已存在，请手动清除后再试\n')
        return None, None

    def add_rust_mod_rs(self, file, mod):
        """
        把 f"mod {mod};" 写入file.
        如果已存在则不写
        """
        cur_mods = []
        if os.path.exists(file):
            with open(file, 'r') as f:
                for line in f.readlines():
                    if line.strip():
                        cur_mods.append(line.strip())  # 读行
        mod = f'mod {mod};'
        if mod not in cur_mods:
            cur_mods.append(mod)
        with open(file, 'w') as f:  # 写回mod.rs里
            for mod in cur_mods:
                if mod:
                    f.write(f'{mod}\n')

    def make_rust_paths(self):
        # 创建rust的主文件和测试文件目录，并同步创建mod.rs

        def create_mod_rs(p, nexts):
            for nxt in nexts:  # 创建新目录或文件时，同时在mod.rs里添加
                mod_file = os.path.join(p, 'mod.rs')
                self.add_rust_mod_rs(mod_file, nxt)
                p = os.path.join(p, nxt)  # 父目录更新

        files_path = os.path.join(RUST_TARGET_DIR, self.site_tag, self.contest, self.task_id)
        if not os.path.exists(files_path):
            os.makedirs(files_path)
            create_mod_rs(os.path.join(RUST_TARGET_DIR, self.site_tag),
                          (self.contest, self.task_id, self.file_name))  # 逐层添加mod.rs
            main_file = os.path.join(files_path, f'{self.file_name}.rs')
            test_file = os.path.join(files_path, f'{self.file_name}_test.rs')
            self.add_rust_mod_rs(os.path.join(files_path, 'mod.rs'), f'{self.file_name}_test')
            return main_file, test_file
        else:
            sys.stderr.write(f'rust: {files_path}已存在，请手动清除后再试\n')
        return None, None

    def make_python_paths(self):
        # 创建py文件的对应目录，但不创建文件，手动挪入py的文件
        files_path = os.path.join(PYTHON_TARGET_DIR, self.site_tag, self.contest, self.task_id)
        if not os.path.exists(files_path):
            os.makedirs(files_path)
            print(f'创建目录成功{files_path}')
            main_file = os.path.join(files_path, f'{self.file_name}.py')
            return main_file
        else:
            sys.stderr.write(f'py: {files_path}已存在，请手动清除后再试\n')
        return None

    def gen_go_main_file(self, file):
        print(f'{file},创建成功')
        with open(file, 'w') as f:
            print(f'创建模板文件{file}成功')
            f.write("""package main

import (
    "bufio"
    . "fmt"
    "io"
    "os"
)

func solve(in io.Reader, out io.Writer) {
	var n, ans int
	Fscan(in, &n)
	a := make([]int, n)
	for i := 0; i < n; i++ {
		Fscan(in, &a[i])
	}
	
	Fprintln(out, ans)
}
func run(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()
	//var t int
	//for Fscan(in, &t); t > 0; t-- {
	//	solve(in, out)
	//}
	solve(in, out)
}

func main() { run(os.Stdin, os.Stdout) }
""")

    def gen_go_test_file(self, file):
        with open(file, 'w', encoding='utf-8') as f:
            print(f'创建测试文件{file}成功')
            cases = []
            for _in, _out in self.spider(self.url).cases().values():
                cases.append(f'{{`{_in}`,`{_out}`}},')
            cases_str = '\n'.join(cases)
            f.write(f"""package main

import (
    "github.com/EndlessCheng/codeforces-go/main/testutil"
    "testing"
)

func Test_run(t *testing.T) {{
    t.Log("Current test is [{self.task_id}]")
    testCases := [][2]string{{
        {cases_str}
    }}
    testutil.AssertEqualStringCase(t, testCases, 0, run)
}}
// 本模板由https://github.com/liuliangcan/play_with_python/blob/main/tools/gen_code_tool/gen_template.py自动生成,在本目录下使用go test进行case测试
// {self.url}
// {self.url}/submit?taskScreenName={self.file_name}            
""")

    def run(self):
        # 生成go的模板文件
        go, test = self.make_go_paths()
        if go:
            self.gen_go_main_file(go)
            self.gen_go_test_file(test)
        rust, test = self.make_rust_paths()
        if rust:
            self.gen_rust_main_file(rust)
            self.gen_rust_test_file(test)
        py = self.make_python_paths()


if __name__ == '__main__':
    url = 'https://atcoder.jp/contests/arc119/tasks/arc119_c'
    BaseGenTemplate(url).run()
