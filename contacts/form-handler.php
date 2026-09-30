<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: https://thnkfor.me');

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['ok' => false, 'error' => 'Method not allowed']);
    exit;
}

$name    = trim(strip_tags($_POST['name'] ?? ''));
$contact = trim(strip_tags($_POST['contact'] ?? ''));
$service = trim(strip_tags($_POST['service'] ?? ''));
$message = trim(strip_tags($_POST['message'] ?? ''));

if (!$name || !$contact) {
    http_response_code(400);
    echo json_encode(['ok' => false, 'error' => 'Заполните обязательные поля']);
    exit;
}

$to = 'hello@thnkfor.me';
$subject = "Новая заявка с сайта — {$name}";

$body  = "Имя: {$name}\n";
$body .= "Контакт: {$contact}\n";
if ($service) $body .= "Услуга: {$service}\n";
if ($message) $body .= "\nОписание:\n{$message}\n";
$body .= "\n---\nОтправлено с thnkfor.me/contacts/";

$headers  = "From: noreply@thnkfor.me\r\n";
$headers .= "Reply-To: {$contact}\r\n";
$headers .= "Content-Type: text/plain; charset=UTF-8\r\n";
$headers .= "X-Mailer: PHP/" . phpversion();

if (mail($to, '=?UTF-8?B?' . base64_encode($subject) . '?=', $body, $headers)) {
    echo json_encode(['ok' => true]);
} else {
    http_response_code(500);
    echo json_encode(['ok' => false, 'error' => 'Ошибка отправки, попробуйте позже']);
}
