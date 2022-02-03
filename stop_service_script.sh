#!/bin/bash

 

ps awx | grep "service_script" | head -n 1 | awk '{print $1}' | xargs -i kill {}

/usr/bin/echo "$(date) Process killed" >> /var/log/tele_bot
