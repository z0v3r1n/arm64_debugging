will have a blog up in some time on arm64 debugging but, for now this is enough ...
there are a bunch of caveats tho ...
you can't run the arm64_dbg.sh two times at the same time while the other one is running ...
and, we do have a bunch of dependencies:

```
sudo apt install qemu-user-static binfmt-support qemu-user gdb-multiarch
```

these scripts have only been tested on kali linux and might possibly break on your system
also, you need to have tmux installed which is already installed by default on kali :D
