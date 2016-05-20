#! /usr/bin/perl
# 
# Copyright (C) 2004-2005 HUNDREDSOFT CORPORATION All Rights Reserved.
#
#  wol.cgi

use Socket;

#### MACアドレスとIPアドレスorグローバルIPアドレス設定 ####
$macaddr = ''; # xx-xx-xx-xx-xx-xx
$ipaddr = '';  # xxx.xxx.xxx.xxx
####################################################

$macaddr=~s/-//g;
$data = &chr16hex($macaddr);

socket(SOCKET, PF_INET, SOCK_DGRAM, 0);
$iaddr = inet_aton($ipaddr);
$sock_addr = pack_sockaddr_in(2304, $iaddr);

send(SOCKET, $data, 0, $sock_addr);


print "Content-type: text/html\n\n";

print<<"HTML";
<html manifest="cache.manifest">
<head>
HTML

print<<"apple-html-setting";
<link rel="apple-touch-icon" href="apple-touch-icon.png" />
<link rel="stylesheet" href="iphone.css" type="text/css" />
<link rel="apple-touch-startup-image" href="loading.png" sizes="640x1096" media="(device-height: 568px)" />
<!--<script type="text/javascript" src="jquery.js"></script>-->
<script type="text/javascript" src="http://code.jquery.com/jquery-1.6.4.min.js"></script>
<script type="text/javascript" src="http://code.jquery.com/mobile/1.0.1/jquery.mobile-1.0.1.min.js"></script>
<link rel="stylesheet" href="http://code.jquery.com/mobile/1.0.1/jquery.mobile-1.0.1.min.css" /> 
<script type="text/javascript" src="iphone.js"></script>
<meta name="viewport" content="width=320.1, user-scalable=no">
<meta name="apple-mobile-web-app-capable" content="yes" />
<meta name="apple-mobile-web-app-status-bar-style" content="black" />
apple-html-setting

print<<"HTML";
<meta http-equiv="Content-Language" content="ja">
<meta http-equiv="Content-Type" content="text/html; charset=x-euc-jp">
HTML

print<<"title";
<title>BOOT START</title>
title

print<<"HTML";

</head>
<body>
<div id="home" data-role="page" data-theme="a">
	<h1>BOOT START</h1>
	<a href="teamviewer8://" data-role="button" data-icon="arrow-r">TeamViewerを起動</a>
</div>
</body>
</html>
HTML


exit;



sub chr16hex {
	local($mac) = @_;
	$_ = "ffffffffffff";
	for ($i=0; $i<16; $i++){
		$_ .= $mac;
	}
	1 while s/([0-9A-Fa-f][0-9A-Fa-f])/pack("c",hex($1))/geo;
	$_;
}


__END__
