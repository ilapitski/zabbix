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
   ansible.playbook = 'provision_vm4.yml'
   ansible.verbose = 'vv'
   end

config.vm.define :vm4 do |vm4|
    vm4.vm.box = "sbeliakou/centos-6.7-x86_64"
    vm4.vm.hostname = "zabbix-vm4"
    vm4.vm.network "private_network", ip: "192.168.33.14"
    #vm4.vm.network "forwarded_port", guest: 80, host: 8181
    #vm4.vm.synced_folder ".", "/vagrant", disabled: true
    #vm4.vm.synced_folder "/root/vagrant/share2", "/vagrant-vm-share", owner: "root", group: "root"
    	vm4.vm.provider "virtualbox" do |vb4|
		vb4.name = "zabbix-vm4"
		vb4.customize ["modifyvm", :id, "--memory", 2048]
		#vb4.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
        end
   end
end
