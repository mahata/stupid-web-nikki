# -*- mode: ruby -*-
# vi: set ft=ruby :
#
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu13"
  config.vm.box_url = "http://cloud-images.ubuntu.com/vagrant/raring/current/raring-server-cloudimg-amd64-vagrant-disk1.box"
  config.vm.hostname = "stupid-web-nikki"
  config.vm.synced_folder "source", "/home/vagrant", :nfs => true
  config.version.url = "dummy"

  config.vm.network :forwarded_port, guest: 22, host: 2201, id: "ssh"
  config.vm.network :forwarded_port, guest: 80, host: 8001, id: "http"
  config.vm.network :private_network, ip: "192.168.1.100"

  config.vm.provider :virtualbox do |vb|
    vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
  end

  config.vm.provision :ansible do |ansible|
    ansible.playbook = "main.yml"
    ansible.inventory_path = "inventories/vagrant"
  end
end