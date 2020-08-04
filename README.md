# LCYSign
良辰云自动签到以获取流量

### Usage
在运行之前先修改**sign.py**文件里面的邮箱和密码，即**email**和**passwd**参数。之后便可以利用**crontab**来设定每天定时执行一次脚本。例如在每天六点零一分的时候运行一次脚本：
> crontab -e
* 在打开的文件中添加如下指令
>  01 06 * * * python3 sign.py

### Contribute
欢迎贡献你的代码。
