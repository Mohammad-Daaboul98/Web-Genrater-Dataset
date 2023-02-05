# Python 3 code to rename multiple
# files in a directory or folder

# importing os module
import os

# Function to rename multiple files
def main():

	folder = "C:\\Users\\basel\\Desktop\\test\\master\\dataset\\about-form-samples"
	for count, filename in enumerate(os.listdir(folder)):
		dst = f"{str(count+500000)}.gui"
		src = f"{folder}/{filename}" # foldername/filename, if .py file is outside folder
		dst = f"{folder}/{dst}"
		
		# rename() function will
		# rename all the files
		os.rename(src, dst)

# Driver Code
if __name__ == '__main__':
	
	# Calling main() function
	main()
