""" Converts the contents of a pinned Pipfile into a executable shell script
    with the applicable `pipenv install ...` commands to rebuild the pipenv
    virtual environment from scratch. """

import os

with open(file='Pipfile', mode='r') as file:

    # Creates the string for the project's [dev-packages] list
    install_str = 'pipenv install'
    for line in file:
        if '[packages]' in line:
            break
        if '==' in line:
            pinned_version = line.replace(' = "', '').replace('"', '').strip('\n')
            install_str += f' {pinned_version}'
        if '*' in line:
            open_version = line.replace(' = "*"', '').strip('\n')
            install_str += f' {open_version}'
    final_dev_packages_install_str = f"{install_str} {'--dev'}"

    # Creates the string for the project's [packages] list
    install_str = 'pipenv install'
    for line in file:
        if '[requires]' in line:
            break
        if '==' in line:
            pinned_version = line.replace(' = "', '').replace('"', '').strip('\n')
            install_str += f' {pinned_version}'
        if '*' in line:
            open_version = line.replace(' = "*"', '').strip('\n')
            install_str += f' {open_version}'
    final_packages_install_str = install_str

    nl = '\n'
    overall_install_str = f"{final_dev_packages_install_str}{nl}{final_packages_install_str}"

    with open(file='pipenv_install.sh', mode='w') as file:
        file.write(overall_install_str)

os.popen('sh pipenv_install.sh')
