# aviso_diario

este código pode servir como um tutorial de como lidar com funções do digital ocean, expressões cron e bots telegram.

a função dele é mandar diariamente uma mensagem em um grupo de telegram, do tipo:

```commandline
Bom dia

Faltam 10 dias para soltar a Lista
Faltam 23 dias para o caça
```

### telegram
[crie um bot de telegram](https://core.telegram.org/bots) e adicione ele ao grupo para o qual você quer que a mensagem seja enviada.
no código, você precisa substituir o token do bot e o id do chat de telegram.
o id do chat está escrito na url depois do #:
`https://web.telegram.org/z/#[id do chat]`


### digital ocean
no digital ocean, vá em manage -> functions e crie uma function.
o código do .py nesse repositório deve ir em source.

a função também deve ter um gatilho, que deve ser adicionado na aba 'trigger'.
o gatilho é programado com uma [expressão cron](https://crontab.guru/#0_12_*_*_*).
para uma mensagem enviada todo dia às 9h da manhã, a expressão cron deve ser (cron são expressos em UTC):
```commandline
0 12 * * *
```