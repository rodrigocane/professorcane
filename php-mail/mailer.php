<?php

//Primeiro passo é criar uma conta no https://www.mailersend.com/. Não se preocupe, é de graça e não precisa informar dados de cartão.
//Próximo passo é gerar um Token. Na tela inicial do Mailersend clique em Integrations > API Tokens > Manage > Create new Token > Sending Acess e no final copia o token
//Finalmente, é hora de instalar o tal do MailerSend conforme descrito em https://developers.mailersend.com/guides/sdk/sending-emails-with-mailersend-and-php.html
//Aí é só adequar o código abaixo ao seu projeto e sucesso!



//Esse arquivo estava em C:\xampp\htdocs\gitcane\php-mail\index.php
//O arquivo autoload.php estava em C:\xampp\php\vendor\autoload.php
//Ou seja, precisei subir 3 diretórios até poder entrar no php/vendor
//Esse require é obrigatório, mas a quantidade de "../" depende de onde este arquivo aqui
//Mas é impossível errar: se você segurar o CONTROL e clicar no autoload.php e não abrir um arquivo, quer dizer que você errou. Coloque mais ou menos "../" até acertar!
require '../../../php/vendor/autoload.php';
use MailerSend\MailerSend;
use MailerSend\Helpers\Builder\Recipient;
use MailerSend\Helpers\Builder\EmailParams;
use MailerSend\Exceptions\MailerSendValidationException;
use MailerSend\Exceptions\MailerSendRateLimitException;

$mailersend = new MailerSend(['api_key' => 'sua chave cadastrada no MailerSend']);
$recipients = [
	new Recipient('pessoa.receber.email@gmail.com', 'Pessoa'),
];

$nome = 'pessoa teste';
$corpo_do_email = '<p>Boa noite, <b>{$nome}</b>.<p>Este é um email personalizado!</p>'; //Veja que no corpo do email podemos utilizar HTML simples

$emailParams = (new EmailParams())
	->setFrom('MS_ybetI4g@ytest-ywjxptoxoxo123.mlsender.net') //seu endereço "FROM" conforme o domínio cadastrado no MailerSend
	->setFromName('Sistema PHP') //nome amigável pra aparecer no e-mail
	->setRecipients($recipients)
	->setSubject('Título do email')
	->setHtml($corpo_do_email);

try {
	$mailersend->email->send($emailParams);
} catch (MailerSendValidationException | MailerSendRateLimitException $e) {
	print_r($e->getErrors());
	print_r($e->getStatusCode());
}

?>
