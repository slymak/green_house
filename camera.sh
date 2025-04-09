#!/usr/bin/bash
today=$(date +%Y-%m-%d_%H:%M)

dirwww=/home/sklep/sklenik
/usr/bin/raspistill -o $dirwww/$today.jpg

function pingserver {
        wget -qO- $1  2>&1
        if [ $? -ne 0 ]
        then
                echo $1 down
        else
                echo $1 live
                rsync -azvh -e "ssh -p 422" $dirwww/*  sklep@$2:/var/www/html/kamera/sklenik \
#                --dry-run
        fi
}

pingserver https://luzicka.slymak.com/digivoltnovakov/check luzicka.slymak.com
pingserver https://slymak.com/digivoltnovakov/check slymak.com

