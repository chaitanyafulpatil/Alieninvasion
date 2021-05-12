if [ "$(uname -m)" = "x86_64" ]; then
                sudo pip3 install pygame
        fi

if [ "$(uname -m)" = "aarch64" ]; then
                sudo apt update
                sudo apt upgrade -y
                sudo apt install -y python3-dev python3-pygame
        fi
