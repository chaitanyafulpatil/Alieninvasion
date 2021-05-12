if [ "$(uname -m)" = "x86_64" ]; then
                sudo pip3 install pygame
        fi
        
if [ "$(uname -m)" = "i686" ]; then
                sudo pip3 install pygame
        fi

if [ "$(uname -m)" = "aarch64" ]; then
                apt update
                apt upgrade -y
                apt install -y python3-dev gcc python3>
        fi

if [ "$(uname -m)" = "armv7l" ]; then
                sudo apt update
                sudo apt upgrade -y
                sudo apt install -y python3-dev python3-pygame
        fi
