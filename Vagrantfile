# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure(2) do |config|

#config.vm.provision "shell", inline: "echo Apache_server_install && yum update -y && yum install -y httpd && chkconfig httpd on && /etc/init.d/httpd start"

# $script = <<SCRIPT
# echo Provisioning...
# echo "192.168.33.10    zabbix-server" >> /etc/hosts
# SCRIPT

# config.vm.provision "shell", inline:$script  # provisioning

config.vm.provision "ansible" do |ansible|
    ansible.playbook = 'provision_zserver.yml'
    ansible.verbose = 'vv'
  end

config.vm.define :zserver do |zserver|
    zserver.vm.box = "sbeliakou/centos-6.7-x86_64"
    zserver.vm.hostname = "zabbix-server"
    zserver.vm.network "private_network", ip: "192.168.33.10"
    #zserver.vm.network "forwarded_port", guest: 80, host: 8181
    #zserver.vm.synced_folder ".", "/vagrant", disabled: true
    #zserver.vm.synced_folder "/root/vagrant/share2", "/vagrant-vm-share", owner: "root", group: "root"
    	zserver.vm.provider "virtualbox" do |zs|
		zs.name = "zabbix-server"
		zs.customize ["modifyvm", :id, "--memory", 4096]
		zs.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
        end
   end
end
