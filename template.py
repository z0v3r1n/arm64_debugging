#!/usr/bin/env python3
from pwn import *
import tempfile, os, subprocess

exe = context.binary = ELF(args.EXE or './chall')
libc = ELF(exe.libc.path)


def start(argv=[], *a, **kw):
    if args.GDB:
        io = process(['qemu-aarch64', '-g', '1234', '-L', '.', exe.path] + argv, *a, **kw)
        gdbinit = tempfile.NamedTemporaryFile(mode='w', delete=False, prefix=".debug_arm64_gdbinit_")
        gdbinit.write(f"""
	set context-sections regs disasm
	set architecture aarch64
	set sysroot "{os.getcwd()}"
	set solib-search-path "{os.getcwd()}"
	file "{exe.path}"
	{init_script}
	target remote :1234
	{"continue" if continue_after_init else ""}
	""")
        gdbinit.flush()
        gdbinit.close()
        subprocess.Popen(['qterminal', '-e', 'gdb-multiarch', '-q', '-x', gdbinit.name, exe.path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return io
    else:
        return process(['qemu-aarch64', '-L', '.', exe.path] + argv, *a, **kw)

continue_after_init = False
init_script = '''
'''

io = start()
io.interactive()

