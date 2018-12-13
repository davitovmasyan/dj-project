### Ansible

This repository is responsible for provisioning and deployment of masaha

* [Install](https://docs.ansible.com/ansible/2.7/installation_guide/intro_installation.html) Ansible
* Copy hosts.ini.dist to hosts.ini
* Replace the placeholder with your server IP (make sure, that you have an ssh access to the server)

### Commands

Deploy

```ansible-playbook playbook.yml -i hosts.ini -l prod -t deploy```

Run all tasks

```ansible-playbook playbook.yml -i hosts.ini -l prod```