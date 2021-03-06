# 补丁Trac Ticket平台参数检查插件使用说明

## 使用对象

该插件的使用对象为Trac平台管理员，非普通用户

## 使用方法

1. 进入含有setup.py文件的目录，执行：python setup.py bdist_egg；
2. 将 dist 目录下的 TracTicketValidator-1.0-pyx.y.egg（x、y指python版本，以具体环境为准） 文件复制到 Trac工程的plugins 目录下；
3. 配置Trac的配置文件trac.ini:

        新增以下内容：

        [TicketValidator]
        summary.rule = .+
        summary.tip = 相同标题的ticket已经存在，禁止重复创建标题完全相同的ticket
        validate_author = true
        validate_flag = true
        validates = summary
4. 重启Trac服务器
   此时新增插件功能即可生效，此时在浏览器登录Trac平台创建ticket，将会发现关键字段非法则无法创建，必须填写完整才运行创建ticket。

## 备注
该插件会持续优化完善，检查字段后期有可能增加，所以trac.ini会相应的进行配置以保证生效。
