from subprocess import call

#Commit Message
commit_message = "Updating json files"

#Stage the file
call('git add .', shell = True)

# Add your commit
call('git commit -m "'+ commit_message +'"', shell = True)

#Push the new or update files
call('git push origin master', shell = True)

