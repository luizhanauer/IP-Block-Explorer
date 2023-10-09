IP Block Explorer
=================

IP Block Explorer é uma aplicação Python que permite pesquisar informações de blocos de endereços IP usando dados do arquivo 'delegated-lacnic-extended-latest' fornecido pela LACNIC.

Instalação
----------

Para usar a aplicação, primeiro é necessário clonar o repositório e instalar as dependências. Para isso, execute os seguintes comandos no terminal:



```
git clone https://github.com/luizhanauer/IP-Block-Explorer.git 
```
```
cd IP-Block-Explorer
```
```
pip install -r requirements.txt
```

Uso
---

Para executar a aplicação, basta rodar o arquivo 'ip\_block\_explorer.py':

Copy code

```
python3 ip_block_explorer.py
```

A aplicação irá baixar o arquivo 'delegated-lacnic-extended-latest' automaticamente, e irá pedir ao usuário que digite o ASN (Autonomous System Number) que deseja pesquisar.

Os resultados da pesquisa serão exibidos em uma tabela, contendo as seguintes informações:

*   Registry: o registro onde o bloco de endereços IP foi alocado
*   CC: o código do país associado ao bloco de endereços IP
*   Type: o tipo de endereço IP (ipv4 ou ipv6)
*   Start Address: o endereço IP de início do bloco
*   Value: o número de endereços IP no bloco
*   Date: a data em que o bloco foi alocado
*   Status: o status do bloco (assigned ou allocated)
*   Opaque ID: o ID opaco associado ao bloco

Exemplo de Uso
--------------

Para pesquisar informações de um bloco de endereços IP associado ao ASN 61599, execute o comando abaixo:

```

██╗██████╗     ██████╗ ██╗      ██████╗  ██████╗██╗  ██╗    ███████╗██╗  ██╗██████╗ ██╗      ██████╗ ██████╗ ███████╗██████╗ 
██║██╔══██╗    ██╔══██╗██║     ██╔═══██╗██╔════╝██║ ██╔╝    ██╔════╝╚██╗██╔╝██╔══██╗██║     ██╔═══██╗██╔══██╗██╔════╝██╔══██╗
██║██████╔╝    ██████╔╝██║     ██║   ██║██║     █████╔╝     █████╗   ╚███╔╝ ██████╔╝██║     ██║   ██║██████╔╝█████╗  ██████╔╝
██║██╔═══╝     ██╔══██╗██║     ██║   ██║██║     ██╔═██╗     ██╔══╝   ██╔██╗ ██╔═══╝ ██║     ██║   ██║██╔══██╗██╔══╝  ██╔══██╗
██║██║         ██████╔╝███████╗╚██████╔╝╚██████╗██║  ██╗    ███████╗██╔╝ ██╗██║     ███████╗╚██████╔╝██║  ██║███████╗██║  ██║
╚═╝╚═╝         ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
by Luiz Hanauer

Digite o ASN que deseja pesquisar os blocos (ou 'q' para sair): 61599

Registry    CC    Type    Start Address      Value      Date  Status       Opaque ID
----------  ----  ------  ---------------  -------  --------  ---------  -----------
lacnic      BR    ipv4    200.71.76.0         1024  20170427  allocated       135068
lacnic      BR    ipv6    2804:3ca0::           32  20170427  allocated       135068

Digite o ASN que deseja pesquisar os blocos (ou 'q' para sair): 


```


Contribuição
------------

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões para melhorar a aplicação, sinta-se à vontade para abrir uma issue ou enviar um pull request.

Se você gostou do meu trabalho e quer me agradecer, você pode me pagar um café :)

<a href="https://www.paypal.com/donate/?hosted_button_id=SFR785YEYHC4E" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 40px !important;width: 150px !important;" ></a>


Licença
-------

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para obter mais informações.
