Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-20.04"
  config.vm.network "forwarded_port", guest: 22, host: 22, auto_correct: true
  config.vm.network "forwarded_port", guest: 80, host: 80, auto_correct: true
  config.vm.network "forwarded_port", guest: 5001, host: 5001, auto_correct: true
  config.vm.provider "vmware_desktop" do |v|
    v.vmx["memsize"] = 4096
    v.vmx["numvcpus"] = 2
  end
  config.vm.provider "virtualbox" do |v|
    v.memory = 4096
    v.cpus = 2
  end  
  config.vm.provision "shell", path: "docker_install.sh"
  config.vm.provision "shell", inline: "echo 'set expandtab\nset tabstop=2' > /home/vagrant/.vimrc"
  config.vm.synced_folder "docker101-apps/", "/home/vagrant/docker101-apps"
end
