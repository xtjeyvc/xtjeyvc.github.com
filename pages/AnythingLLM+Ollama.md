- 最近在测试在本地离线环境下的个人知识库，要求支持本地大语言模型，支持doc、excel、md、pdf以及各种图片，可以对于知识库里面的相关的材料进行解析，根据模版材料和材料清单生成相关法律文书或材料。
  
  测试过的模型包括：通义千问Qwen2的7B、llama3 7B，bunny llama3的修改版。
  
  测试过的LLM软件有：Qanything、langchain、dify、anythingLLM等。
  
  结合本地笔记软件测试过WPSai、notionAI、obsidian的AI插件等等
  
  正常使用AI工具一般来讲是有硬件要求的，如果不是英伟达的30/40系列显卡，显存至少8G以上，使用本地语言模型是有些困难的，只能使用网络版或者通过API；如果硬件要求达标，向我个人使用的是 I5 12400+3070 8G,这个硬件组合基本上也可以使用个10年没有什么问题的。
- #### [AnythingLLM的介绍](https://www.ibiji.cn/#/home/ai-ad?id=anythingllm%e7%9a%84%e4%bb%8b%e7%bb%8d)
- 1、官网：[https://useanything.com/](https://useanything.com/)
- 2、AnythingLLM是一款由Mintplex Labs Inc.开发的开源工具，它相当于一个私有的ChatGPT或其他大型语言模型（LLMs）应用，专为在安全的环境内与文档或其他内容进行智能聊天而设计。这款工具的主要特点包括：
	- 1）. **开源与可定制性**：作为开源软件，AnythingLLM允许用户根据自身需求进行高度定制，无论是调整模型参数、集成特定的数据源还是优化工作流程。
	- 2）. **高效的企业级解决方案**：适用于企业环境，能够将广泛的文档、资源或内容片段转化为可交互的知识库，提高信息查询和利用的效率。
	- 3）. **与现有文档集成**：能够轻松地与现有的文档、数据库或其他内容管理系统集成，让用户能够直接通过聊天界面访问和查询这些资源。
	- 4）. **支持多种大型语言模型**：兼容多种开源和商业化的大语言模型，提供了灵活性，用户可以根据自己的资源和需求选择合适的模型。
	- 5）. **本地部署能力**：结合Ollama等工具，AnythingLLM可以在本地环境中部署，确保数据的安全性和隐私保护，避免了将敏感信息上传到云端的需要。
	- 6）. **简易配置与部署**：提供了直观的配置界面，如通过指定LLM服务地址（如Ollama的`http://127.0.0.1:11434`）、选择模型版本（如`qwen:4b`）和设置其他参数，使得部署过程相对简便。
	  
	  综上所述，AnythingLLM是一个强大且灵活的工具，适合那些希望在控制数据的同时，利用AI技术提升知识管理和信息检索体验的个人和组织。
- #### [Ollama的介绍](https://www.ibiji.cn/#/home/ai-ad?id=ollama%e7%9a%84%e4%bb%8b%e7%bb%8d)
- 1、官网： [https://ollama.com/](https://ollama.com/)
- 2、模型库：[https://ollama.com/library](https://ollama.com/library)
- 3、OLLAMA是一个开源项目，它旨在为用户提供一个简便的方式来部署和使用大型语言模型（LLMs）。OLLAMA是面向开发者和研究人员的一个强大工具，它降低了部署和操作大型语言模型的难度，同时提供了高度的灵活性和易用性，促进了AI技术的普及和创新应用。
- #### [使用](https://www.ibiji.cn/#/home/ai-ad?id=%e4%bd%bf%e7%94%a8)
- 1、下载安装Ollama
- 2、到Ollama的模型库找到模型，比如千问7B 在本地命令框里输入 ollama run qwen2:7b 下载千问7B模型
- 3、安装anythingLLM查看基本用法 [https://docs.useanything.com/](https://docs.useanything.com/)