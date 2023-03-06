## 使用方法
1. 准备环境并部署到vercel
```shell
brew install node
npm i -g vercel
git clone
cd openai-api

vercel login
vercel -A openai.json --prod
```
2. 去 vercel 的 dashboard 修改你自己的 domain 
3. 修改 chat. py 中的 api-key 和 url(改成你自己的domain) 
4. python chat.py