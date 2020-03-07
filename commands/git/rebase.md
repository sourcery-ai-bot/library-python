# Rebase Subsidiary Branch With That of Its Parent

**Scenario**: If I would like to rebaseline the `develop` branch with that of the `master`, the following workflow can be used.

This would be most often completed if the parent branch has been updated with some fixes and I would like to ensure that the `develop` branch is a reflection of the `master`.

#### Step 1

```sh
git checkout develop
```

#### Step 2

```sh
git rebase master
```

Source: <https://stackoverflow.com/questions/5340724/get-changes-from-master-into-branch-in-git/5340773>
