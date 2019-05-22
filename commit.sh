
#!/bin/bash

git pull origin master && $SOLO/create.sh /Users/turvo/turvo/ops/live/us-west-2/development/$1.json && git add us-west-2/development/$1.json && git commit -m "deploy :: Deploy $1 to development for @sanjeev.d" && git push origin master
