### 内网穿透



#### **一、Tailscale**

- https://login.tailscale.com/admin/welcome

- 个人服务器：系统:Debian GNU/Linux 9 armv7l(Py3.7.8)

- 安装脚本：

- ```
  curl -fsSL https://tailscale.com/install.sh | sh
  ```

- 一键更新软件源脚本

- ```
  国内用：
  bash <(curl -sSL https://linuxmirrors.cn/main.sh)
  教育网用：
  bash <(curl -sSL https://linuxmirrors.cn/main.sh) --edu
  国外用：
  bash <(curl -sSL https://linuxmirrors.cn/main.sh) --abroad
  ```

- 更新软件列表

- ```
  sudo apt-get update
  ```

- 更新软件包

- ```
  sudo apt-get upgrade
  ```

  

#### **二、Zerotier** 

连接ssh直接输入命令行

curl -s https://install.zerotier.com | sudo bash

等待到 success的字样即可再 输入，把第一步创建设备的ID添加进来

zerotier-cli join 自己的NetWork ID

看到200 即添加成功

这里要记住每一个设备 添加完成后需要 zerotier网站 