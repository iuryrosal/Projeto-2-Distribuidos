
As imagens abaixo contém detalhes a respeito das ferramentas utilizadas e das estruturas usadas para funcionamento do projeto:

![image](https://user-images.githubusercontent.com/36707351/114312948-f2a67a80-9aca-11eb-8614-c13e326933d5.png)

![image](https://user-images.githubusercontent.com/36707351/114312957-fc2fe280-9aca-11eb-82ed-910bb24b2f42.png)

![image](https://user-images.githubusercontent.com/36707351/114312967-02be5a00-9acb-11eb-9435-e22627533439.png)

![image](https://user-images.githubusercontent.com/36707351/114312975-0b169500-9acb-11eb-9f9e-e9131220cdd4.png)

![image](https://user-images.githubusercontent.com/36707351/114312982-110c7600-9acb-11eb-8b58-5d8e1fa4b79f.png)

![image](https://user-images.githubusercontent.com/36707351/114312994-17025700-9acb-11eb-91b8-de0c7e5c36c7.png)

![image](https://user-images.githubusercontent.com/36707351/114312999-1cf83800-9acb-11eb-84ec-f67c5d280a4e.png)

![image](https://user-images.githubusercontent.com/36707351/114313007-22558280-9acb-11eb-9405-8951ecdf59d1.png)

O arquivo proto contém as informações sobre o formato das mensagens trocadas via GRPC entre o Home Assistant e os objetos. ObjectService é uma generalização que é herdada por todos os objetos, tendo a opção de ligar e desligar o objeto, bem como alterar a sua variável que afetará o ambiente.
![image](https://user-images.githubusercontent.com/36707351/114313011-27b2cd00-9acb-11eb-9520-04da0d8272b3.png)

![image](https://user-images.githubusercontent.com/36707351/114313020-2da8ae00-9acb-11eb-8d9e-949ed3b1e823.png)

A classe ObjectService especifica como ocorrerá a execução desses métodos remotos que irá utilizar dos métodos locais de cada objeto para afetar seu status conforme o método remoto gerado via GRPC.
![image](https://user-images.githubusercontent.com/36707351/114313027-35685280-9acb-11eb-893d-ef129010169d.png)

![image](https://user-images.githubusercontent.com/36707351/114313031-3ac59d00-9acb-11eb-9ec1-b5ba054671c8.png)

![image](https://user-images.githubusercontent.com/36707351/114313039-41541480-9acb-11eb-827f-2df54c3e7f26.png)
