#!/bin/sh
if [ -z "$1" ]; then exit 1 ; fi

cat > "/tmp/.debug_arm64_gdbinit" <<EOF
set context-sections regs disasm
set architecture aarch64
set sysroot "$(pwd)"
set solib-search-path "$(pwd)"
file "$(readlink -f "$1")"
target remote :1234
EOF

tmux new-session -d -s "arm64_dbg" "bash -lc 'qemu-aarch64 -g 1234 -L . \"$(readlink -f "$1")\"'"
tmux split-window -t "arm64_dbg:0" -v "bash -lc 'sleep 0.15; gdb-multiarch -q -x \"/tmp/.debug_arm64_gdbinit\" $(readlink -f \"$1\")'"
tmux select-layout -t "arm64_dbg:0" tiled

tmux resize-pane -t "arm64_dbg:0.1" -D 10
tmux swap-pane -t "arm64_dbg:0" -U

tmux attach -t arm64_dbg
