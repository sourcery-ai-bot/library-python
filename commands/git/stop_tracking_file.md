# Stop Tracking File

`.gitignore` will prevent untracked files from being added (without an add -f) to the set of files tracked by git, however git will continue to track any files that are already being tracked.

To stop tracking a file, I need to remove it from the index. This can be achieved with the following command.

```sh
git rm --cached <filename>
```

If I would like to remove an entire directory, I need to remove all files in it recursively.

```sh
git rm -r --cached <folder-name>
```

The removal of the file from the head revision will happen on the next commit.

<span style="color: red;">WARNING:</span> While this will not remove the physical file from my local, it will remove the files from other developer's machines on next `git pull`.

Source: <https://stackoverflow.com/questions/1274057/how-to-make-git-forget-about-a-file-that-was-tracked-but-is-now-in-gitignore>
