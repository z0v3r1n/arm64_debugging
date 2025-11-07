I’ll be writing a proper blog post on arm64 debugging on amd64 machine soon, but for now this should be enough to get going.

There *are* a few caveats, though:

* you **cannot** run `arm64_dbg.sh` multiple times in parallel — only one instance can be active at a time
* there are some dependencies you need installed first:

```bash
sudo apt install qemu-user-static binfmt-support qemu-user gdb-multiarch
```

This was only tested on kali linux — it *may* work fine elsewhere, but no promises.

You’ll also need `tmux` — it’s preinstalled on kali, but if you’re on another distro you’ll need to install it manually.
