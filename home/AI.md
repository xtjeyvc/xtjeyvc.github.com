### AI相关

纪检工作的尽头是物理，要想作好纪检监察工作首先就要学好物理，因为本质上纪检监察工作的本质在于从信息载体上提取各类信息，并制作出符合法定形式的信息复制品，对于信息的理解是影响我们对于纪检工作的认识。

2022年11月30日随着chatGPT的发布，随着这一类大语言模型的发展，人类社会现在已经进入新的时期，拥抱AI是身处这个时代的每一个人都需要面对的事情，AI对于人类社会的改变更多的体现在AI模拟处理人类活动决策逻辑过程，以一种客观化的方式来体现各类决策的过程。大语言模型的最大意义在于将公开领域的知识进行了大集成，人人可以平等的学习和掌握公开领域的知识信息而不是被垄断，解决问题的能力更多的体现在了提出问题的能力，就这一点而言，对于人才培养、素质教育等领域都是一些重大的变更。

面前而言，AI对于程序员、设计行业、新媒体行业、文字工作者等冲击较大，对于垄断性行业（对于效率提高不敏感）、政府机关等影响目前来讲是比较小，对于体力劳动者影响小，但随着AI的发展对于社会形态的重构，就职业技能掌握而言，而个人建议是越多越多，不要进行自我设限，法律、审计、会计、绘画、心理学、医学、工程、佛学、哲学、命理、中医等等领域均可以有所涉猎。

#### 一、AI工具

| 名称     | 特点                                                         | 备注   |
| -------- | ------------------------------------------------------------ | ------ |
| ChatGPT  | https://openai.com/blog/chatgpt/                             | OpenAI |
| Bard     | https://ai.google.com                                        | Google |
| New Bing       | https://browserdefaults.microsoft.com/instructionspage/gcnew/ |   |
| 文心一言 | https://yiyan.baidu.com/welcome                              |        |
| 星火模型 | https://xinghuo.xfyun.cn/                                    |        |
| 通义千问 | https://tongyi.aliyun.com/                                   |        |
| Qanything | https://qanything.ai/                                   |        |

注：国内大模型的编程效果不太理想，特别是python、VBA这类的代码,网易有道的qanything最近新出，支持本地化部署，要求显存8G，内存32G，运行效果挺好。

更新：2024年6月份，通义千问开源版本[qwen 2](https://qwenlm.github.io/zh/blog/qwen2/) 发布，个人使用的是qwen 2 7b的版本，运行非常流畅，相较于原来使用的llama3，在回答质量上有了提高。

| 模型              | Qwen2-0.5B | Qwen2-1.5B | **Qwen2-7B** | Qwen2-57B-A14B | Qwen2-72B |
| :---------------- | :--------: | :--------: | :------: | :------------: | :-------: |
| 参数量            |   0.49B    |   1.54B    |  7.07B   |     57.41B     |  72.71B   |
| 非Embedding参数量 |   0.35B    |   1.31B    |  5.98B   |     56.32B     |  70.21B   |
| GQA               |    True    |    True    |   True   |      True      |   True    |
| Tie Embedding     |    True    |    True    |  False   |     False      |   False   |
| 上下文长度        |    32K     |    32K     |   **128K**   |      64K       |   **128K**    |

在Qwen1.5系列中，只有32B和110B的模型使用了GQA。这一次，所有尺寸的模型都使用了GQA，以便让大家体验到GQA带来的推理加速和显存占用降低的优势。
![img](https://qianwen-res.oss-accelerate-overseas.aliyuncs.com/assets/blog/qwen2/qwen2-72b.jpg#center)

#### 二、其他汇总

- [AI工具集](https://ai-bot.cn/)
- [AI工具集导航](https://www.ai-zip.com/)
- [AI 导航站 ](https://www.naviai.cn/)

#### 三、支持本地部署的模型

- 惠普BookPro 14  AI芯片
- 30/40系列显卡的电脑（显存不低于8G），支持运行**chat with RTX**,支持本地运行大语言模型，数据隐私保护性好。
- AnythingLLm +Ollama 这一套就可以，安装模型qwen2
