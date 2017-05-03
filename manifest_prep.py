#Script used post msub-md5 to check outs, and then creates a Manifest file
#enter number of files 
file_num="$1"

if  ((`find . -name '*.out' -size 0 | xargs ls | wc -l` == $file_num)); then
	echo "$file_num MD5_s were generated"
	echo `find . -name '*.out' -size 0 | xargs rm`
	fi
	if (( `(find . -name '*.out' | wc -l )`  == 0 )); then
	        echo "All outs have been erased will ensure Manifest contains correct number of samples"
	fi
	if  (( `cat *md5 | tee Manifest.txt | wc -l `  == $samples)); then
			echo "Manifest has been created succeffully"
        else
	echo " ERROR. There are below $file_num MD5s..."

        fi
  #error is that it is making the Manifest script but is not making the copy in the spot it is supposed to be made
