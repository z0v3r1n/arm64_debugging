I’ll be writing a proper blog post on arm64 debugging on amd64 machine soon, but for now this should be enough to get going.

There *are* a few caveats, though:

* you **cannot** run `arm64_dbg.sh` multiple times in parallel — only one instance can be active at a time
* there are some dependencies you need installed first:

```bash
sudo apt install qemu-user-static binfmt-support qemu-user gdb-multiarch
```

This was only tested on kali linux — it *may* work fine elsewhere, but no promises.

You’ll also need `tmux` — it’s preinstalled on kali, but if you’re on another distro you’ll need to install it manually.

---

You can run the script like this:

```
./arm64_dbg.sh <binary>
```

For the script just change the binary name from `./chall` to your binaries name. Also, remove these lines if you don't have a libc files provided to you by the challenge:

```python
        set sysroot "{os.getcwd()}"
        set solib-search-path "{os.getcwd()}"
```

Your breakpoints go into the init_script ... And, if you want execution to continue automatically after the initial setup set `continue_after_init` to `True`.
