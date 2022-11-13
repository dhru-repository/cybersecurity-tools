awk 'BEGIN {print "Hello from awktutorial.awk file"}' #awktutorial.awk
# hashtag are used to write comment inside awk script and even in terminal 


awk 'BEGIN {print "printing dpkg.log file"}'
awk '{print $0}' dpkg.log #print dpkg.log file field 0 to print entire file
awk '{print $0}' grid.txt #print grid file
awk '{print $1}' grid.txt #print first column for the grid.
awk '{print $2}' grid.txt #print second column for the grid.
awk '{print $3}' grid.txt #print third column for the grid.
awk '{print $4}' grid.txt #print fourth column for the grid.
awk '{print NF}' grid.txt #identify field in each line
awk '{print NR}' grid.txt #prints out line numbers
awk '{print $1}' dpkg.log
awk 'BEGIN { for (i = 1; i <= 5; ++i) print i }' # for loop in awk
#awk '{ printf("%04d\n", $1) }'
awk 'BEGIN {print "Comma seperator"}'
awk -F',' '{print $1}' grid.txt


