00000a0b <handle_client_bis>:
     a0b:	55                   	push   %ebp
     a0c:	89 e5                	mov    %esp,%ebp
     a0e:	53                   	push   %ebx
     a0f:	83 ec 54             	sub    $0x54,%esp
     a12:	e8 c9 fe ff ff       	call   8e0 <__x86.get_pc_thunk.bx>
     a17:	81 c3 65 25 00 00    	add    $0x2565,%ebx
     a1d:	8b 45 08             	mov    0x8(%ebp),%eax
     a20:	89 45 c4             	mov    %eax,-0x3c(%ebp)
     a23:	65 a1 14 00 00 00    	mov    %gs:0x14,%eax
     a29:	89 45 f4             	mov    %eax,-0xc(%ebp)
     a2c:	31 c0                	xor    %eax,%eax
     a2e:	c7 45 cc 00 00 00 00 	movl   $0x0,-0x34(%ebp)
     a35:	eb 0f                	jmp    a46 <handle_client_bis+0x3b>
     a37:	8d 55 d4             	lea    -0x2c(%ebp),%edx
     a3a:	8b 45 cc             	mov    -0x34(%ebp),%eax
     a3d:	01 d0                	add    %edx,%eax
     a3f:	c6 00 00             	movb   $0x0,(%eax)
     a42:	83 45 cc 01          	addl   $0x1,-0x34(%ebp)
     a46:	83 7d cc 1f          	cmpl   $0x1f,-0x34(%ebp)
     a4a:	7e eb                	jle    a37 <handle_client_bis+0x2c>
     a4c:	c7 83 c4 00 00 00 47 	movl   $0x65766947,0xc4(%ebx)
     a53:	69 76 65
     a56:	c7 83 c8 00 00 00 20 	movl   $0x20656d20,0xc8(%ebx)
     a5d:	6d 65 20
     a60:	c7 83 cc 00 00 00 79 	movl   $0x72756f79,0xcc(%ebx)
     a67:	6f 75 72
     a6a:	c7 83 d0 00 00 00 20 	movl   $0x6d616e20,0xd0(%ebx)
     a71:	6e 61 6d
     a74:	c7 83 d4 00 00 00 65 	movl   $0x203a65,0xd4(%ebx)
     a7b:	3a 20 00
     a7e:	8d 83 c4 00 00 00    	lea    0xc4(%ebx),%eax
     a84:	89 44 24 04          	mov    %eax,0x4(%esp)
     a88:	8b 45 c4             	mov    -0x3c(%ebp),%eax
     a8b:	89 04 24             	mov    %eax,(%esp)
     a8e:	e8 a6 01 00 00       	call   c39 <fsend>
     a93:	8d 83 c4 00 00 00    	lea    0xc4(%ebx),%eax
     a99:	89 44 24 04          	mov    %eax,0x4(%esp)
     a9d:	8b 45 c4             	mov    -0x3c(%ebp),%eax
     aa0:	89 04 24             	mov    %eax,(%esp)
     aa3:	e8 dd 00 00 00       	call   b85 <frecv>
     aa8:	89 45 d0             	mov    %eax,-0x30(%ebp)
     aab:	c7 45 cc 00 00 00 00 	movl   $0x0,-0x34(%ebp)
     ab2:	eb 1c                	jmp    ad0 <handle_client_bis+0xc5>
     ab4:	8d 93 c4 00 00 00    	lea    0xc4(%ebx),%edx
     aba:	8b 45 cc             	mov    -0x34(%ebp),%eax
     abd:	01 d0                	add    %edx,%eax
     abf:	0f b6 00             	movzbl (%eax),%eax
     ac2:	8d 4d d4             	lea    -0x2c(%ebp),%ecx
     ac5:	8b 55 cc             	mov    -0x34(%ebp),%edx
     ac8:	01 ca                	add    %ecx,%edx
     aca:	88 02                	mov    %al,(%edx)
     acc:	83 45 cc 01          	addl   $0x1,-0x34(%ebp)
     ad0:	8b 45 cc             	mov    -0x34(%ebp),%eax
     ad3:	3b 45 d0             	cmp    -0x30(%ebp),%eax
     ad6:	7c dc                	jl     ab4 <handle_client_bis+0xa9>
     ad8:	8d 45 d4             	lea    -0x2c(%ebp),%eax
     adb:	89 44 24 0c          	mov    %eax,0xc(%esp)
     adf:	8d 83 e4 e0 ff ff    	lea    -0x1f1c(%ebx),%eax
     ae5:	89 44 24 08          	mov    %eax,0x8(%esp)
     ae9:	c7 44 24 04 96 00 00 	movl   $0x96,0x4(%esp)
     af0:	00
     af1:	8d 83 c4 00 00 00    	lea    0xc4(%ebx),%eax
     af7:	89 04 24             	mov    %eax,(%esp)
     afa:	e8 21 fd ff ff       	call   820 <snprintf@plt>
     aff:	8d 83 c4 00 00 00    	lea    0xc4(%ebx),%eax
     b05:	89 44 24 04          	mov    %eax,0x4(%esp)
     b09:	8b 45 c4             	mov    -0x3c(%ebp),%eax
     b0c:	89 04 24             	mov    %eax,(%esp)
     b0f:	e8 25 01 00 00       	call   c39 <fsend>
     b14:	8b 45 f4             	mov    -0xc(%ebp),%eax
     b17:	65 33 05 14 00 00 00 	xor    %gs:0x14,%eax
     b1e:	74 05                	je     b25 <handle_client_bis+0x11a>
     b20:	e8 0b 05 00 00       	call   1030 <__stack_chk_fail_local>
     b25:	83 c4 54             	add    $0x54,%esp
     b28:	5b                   	pop    %ebx
     b29:	5d                   	pop    %ebp
     b2a:	c3                   	ret

00000b2b <handle_client>:
     b2b:	55                   	push   %ebp
     b2c:	89 e5                	mov    %esp,%ebp
     b2e:	53                   	push   %ebx
     b2f:	83 ec 24             	sub    $0x24,%esp
     b32:	e8 a9 fd ff ff       	call   8e0 <__x86.get_pc_thunk.bx>
     b37:	81 c3 45 24 00 00    	add    $0x2445,%ebx
     b3d:	8b 45 08             	mov    0x8(%ebp),%eax
     b40:	89 45 e4             	mov    %eax,-0x1c(%ebp)
     b43:	65 a1 14 00 00 00    	mov    %gs:0x14,%eax
     b49:	89 45 f4             	mov    %eax,-0xc(%ebp)
     b4c:	31 c0                	xor    %eax,%eax
     b4e:	8b 45 e4             	mov    -0x1c(%ebp),%eax
     b51:	89 04 24             	mov    %eax,(%esp)
     b54:	e8 b2 fe ff ff       	call   a0b <handle_client_bis>
     b59:	8d 83 ee e0 ff ff    	lea    -0x1f12(%ebx),%eax
     b5f:	89 44 24 04          	mov    %eax,0x4(%esp)
     b63:	8b 45 e4             	mov    -0x1c(%ebp),%eax
     b66:	89 04 24             	mov    %eax,(%esp)
     b69:	e8 cb 00 00 00       	call   c39 <fsend>
     b6e:	8b 45 f4             	mov    -0xc(%ebp),%eax
     b71:	65 33 05 14 00 00 00 	xor    %gs:0x14,%eax
     b78:	74 05                	je     b7f <handle_client+0x54>
     b7a:	e8 b1 04 00 00       	call   1030 <__stack_chk_fail_local>
     b7f:	83 c4 24             	add    $0x24,%esp
     b82:	5b                   	pop    %ebx
     b83:	5d                   	pop    %ebp
     b84:	c3                   	ret

00000b85 <frecv>:
     b85:	55                   	push   %ebp
     b86:	89 e5                	mov    %esp,%ebp
     b88:	53                   	push   %ebx
     b89:	83 ec 34             	sub    $0x34,%esp
     b8c:	e8 4f fd ff ff       	call   8e0 <__x86.get_pc_thunk.bx>
     b91:	81 c3 eb 23 00 00    	add    $0x23eb,%ebx
     b97:	8b 45 08             	mov    0x8(%ebp),%eax
     b9a:	89 45 e4             	mov    %eax,-0x1c(%ebp)
     b9d:	8b 45 0c             	mov    0xc(%ebp),%eax
     ba0:	89 45 e0             	mov    %eax,-0x20(%ebp)
     ba3:	65 a1 14 00 00 00    	mov    %gs:0x14,%eax
     ba9:	89 45 f4             	mov    %eax,-0xc(%ebp)
     bac:	31 c0                	xor    %eax,%eax
     bae:	c7 45 f0 ff ff ff ff 	movl   $0xffffffff,-0x10(%ebp)
     bb5:	c7 44 24 0c 00 00 00 	movl   $0x0,0xc(%esp)
     bbc:	00
     bbd:	c7 44 24 08 96 00 00 	movl   $0x96,0x8(%esp)
     bc4:	00
     bc5:	8b 45 e0             	mov    -0x20(%ebp),%eax
     bc8:	89 44 24 04          	mov    %eax,0x4(%esp)
     bcc:	8b 45 e4             	mov    -0x1c(%ebp),%eax
     bcf:	89 04 24             	mov    %eax,(%esp)
     bd2:	e8 99 fc ff ff       	call   870 <recv@plt>
     bd7:	89 45 f0             	mov    %eax,-0x10(%ebp)
     bda:	83 7d f0 ff          	cmpl   $0xffffffff,-0x10(%ebp)
     bde:	75 0d                	jne    bed <frecv+0x68>
     be0:	8b 45 e0             	mov    -0x20(%ebp),%eax
     be3:	c6 00 00             	movb   $0x0,(%eax)
     be6:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
     beb:	eb 35                	jmp    c22 <frecv+0x9d>
     bed:	8b 45 f0             	mov    -0x10(%ebp),%eax
     bf0:	8d 50 ff             	lea    -0x1(%eax),%edx
     bf3:	8b 45 e0             	mov    -0x20(%ebp),%eax
     bf6:	01 d0                	add    %edx,%eax
     bf8:	0f b6 00             	movzbl (%eax),%eax
     bfb:	3c 0a                	cmp    $0xa,%al
     bfd:	75 04                	jne    c03 <frecv+0x7e>
     bff:	83 6d f0 01          	subl   $0x1,-0x10(%ebp)
     c03:	8b 45 f0             	mov    -0x10(%ebp),%eax
     c06:	89 44 24 08          	mov    %eax,0x8(%esp)
     c0a:	8b 45 e0             	mov    -0x20(%ebp),%eax
     c0d:	89 44 24 04          	mov    %eax,0x4(%esp)
     c11:	8d 83 f4 e0 ff ff    	lea    -0x1f0c(%ebx),%eax
     c17:	89 04 24             	mov    %eax,(%esp)
     c1a:	e8 21 fb ff ff       	call   740 <printf@plt>
     c1f:	8b 45 f0             	mov    -0x10(%ebp),%eax
     c22:	8b 4d f4             	mov    -0xc(%ebp),%ecx
     c25:	65 33 0d 14 00 00 00 	xor    %gs:0x14,%ecx
     c2c:	74 05                	je     c33 <frecv+0xae>
     c2e:	e8 fd 03 00 00       	call   1030 <__stack_chk_fail_local>
     c33:	83 c4 34             	add    $0x34,%esp
     c36:	5b                   	pop    %ebx
     c37:	5d                   	pop    %ebp
     c38:	c3                   	ret

00000c39 <fsend>:
     c39:	55                   	push   %ebp
     c3a:	89 e5                	mov    %esp,%ebp
     c3c:	53                   	push   %ebx
     c3d:	83 ec 34             	sub    $0x34,%esp
     c40:	e8 9b fc ff ff       	call   8e0 <__x86.get_pc_thunk.bx>
     c45:	81 c3 37 23 00 00    	add    $0x2337,%ebx
     c4b:	8b 45 08             	mov    0x8(%ebp),%eax
     c4e:	89 45 e4             	mov    %eax,-0x1c(%ebp)
     c51:	8b 45 0c             	mov    0xc(%ebp),%eax
     c54:	89 45 e0             	mov    %eax,-0x20(%ebp)
     c57:	65 a1 14 00 00 00    	mov    %gs:0x14,%eax
     c5d:	89 45 f4             	mov    %eax,-0xc(%ebp)
     c60:	31 c0                	xor    %eax,%eax
     c62:	8b 45 e0             	mov    -0x20(%ebp),%eax
     c65:	89 04 24             	mov    %eax,(%esp)
     c68:	e8 73 fb ff ff       	call   7e0 <strlen@plt>
     c6d:	89 45 f0             	mov    %eax,-0x10(%ebp)
     c70:	83 7d f0 20          	cmpl   $0x20,-0x10(%ebp)
     c74:	7e 15                	jle    c8b <fsend+0x52>
     c76:	c7 45 f0 20 00 00 00 	movl   $0x20,-0x10(%ebp)
     c7d:	8b 45 f0             	mov    -0x10(%ebp),%eax
     c80:	8d 50 ff             	lea    -0x1(%eax),%edx
     c83:	8b 45 e0             	mov    -0x20(%ebp),%eax
     c86:	01 d0                	add    %edx,%eax
     c88:	c6 00 0a             	movb   $0xa,(%eax)
     c8b:	8b 45 e0             	mov    -0x20(%ebp),%eax
     c8e:	89 44 24 04          	mov    %eax,0x4(%esp)
     c92:	8d 83 06 e1 ff ff    	lea    -0x1efa(%ebx),%eax
     c98:	89 04 24             	mov    %eax,(%esp)
     c9b:	e8 a0 fa ff ff       	call   740 <printf@plt>
     ca0:	8b 45 f0             	mov    -0x10(%ebp),%eax
     ca3:	c7 44 24 0c 00 00 00 	movl   $0x0,0xc(%esp)
     caa:	00
     cab:	89 44 24 08          	mov    %eax,0x8(%esp)
     caf:	8b 45 e0             	mov    -0x20(%ebp),%eax
     cb2:	89 44 24 04          	mov    %eax,0x4(%esp)
     cb6:	8b 45 e4             	mov    -0x1c(%ebp),%eax
     cb9:	89 04 24             	mov    %eax,(%esp)
     cbc:	e8 cf fb ff ff       	call   890 <send@plt>
     cc1:	8b 4d f4             	mov    -0xc(%ebp),%ecx
     cc4:	65 33 0d 14 00 00 00 	xor    %gs:0x14,%ecx
     ccb:	74 05                	je     cd2 <fsend+0x99>
     ccd:	e8 5e 03 00 00       	call   1030 <__stack_chk_fail_local>
     cd2:	83 c4 34             	add    $0x34,%esp
     cd5:	5b                   	pop    %ebx
     cd6:	5d                   	pop    %ebp
     cd7:	c3                   	ret

00000cd8 <main>:
     cd8:	55                   	push   %ebp
     cd9:	89 e5                	mov    %esp,%ebp
     cdb:	53                   	push   %ebx
     cdc:	83 e4 f0             	and    $0xfffffff0,%esp
     cdf:	83 ec 70             	sub    $0x70,%esp
     ce2:	e8 f9 fb ff ff       	call   8e0 <__x86.get_pc_thunk.bx>
     ce7:	81 c3 95 22 00 00    	add    $0x2295,%ebx
     ced:	8b 45 08             	mov    0x8(%ebp),%eax
     cf0:	89 44 24 1c          	mov    %eax,0x1c(%esp)
     cf4:	8b 45 0c             	mov    0xc(%ebp),%eax
     cf7:	89 44 24 18          	mov    %eax,0x18(%esp)
     cfb:	8b 45 10             	mov    0x10(%ebp),%eax
     cfe:	89 44 24 14          	mov    %eax,0x14(%esp)
     d02:	65 a1 14 00 00 00    	mov    %gs:0x14,%eax
     d08:	89 44 24 6c          	mov    %eax,0x6c(%esp)
     d0c:	31 c0                	xor    %eax,%eax
     d0e:	83 7c 24 1c 02       	cmpl   $0x2,0x1c(%esp)
     d13:	74 24                	je     d39 <main+0x61>
     d15:	8b 44 24 18          	mov    0x18(%esp),%eax
     d19:	8b 00                	mov    (%eax),%eax
     d1b:	89 44 24 04          	mov    %eax,0x4(%esp)
     d1f:	8d 83 0d e1 ff ff    	lea    -0x1ef3(%ebx),%eax
     d25:	89 04 24             	mov    %eax,(%esp)
     d28:	e8 13 fa ff ff       	call   740 <printf@plt>
     d2d:	c7 04 24 01 00 00 00 	movl   $0x1,(%esp)
     d34:	e8 97 fa ff ff       	call   7d0 <exit@plt>
     d39:	c7 44 24 04 01 00 00 	movl   $0x1,0x4(%esp)
     d40:	00
     d41:	c7 04 24 11 00 00 00 	movl   $0x11,(%esp)
     d48:	e8 63 fa ff ff       	call   7b0 <__sysv_signal@plt>
     d4d:	83 f8 ff             	cmp    $0xffffffff,%eax
     d50:	75 1a                	jne    d6c <main+0x94>
     d52:	8d 83 23 e1 ff ff    	lea    -0x1edd(%ebx),%eax
     d58:	89 04 24             	mov    %eax,(%esp)
     d5b:	e8 40 fa ff ff       	call   7a0 <puts@plt>
     d60:	c7 04 24 01 00 00 00 	movl   $0x1,(%esp)
     d67:	e8 64 fa ff ff       	call   7d0 <exit@plt>
     d6c:	8b 44 24 18          	mov    0x18(%esp),%eax
     d70:	83 c0 04             	add    $0x4,%eax
     d73:	8b 00                	mov    (%eax),%eax
     d75:	89 04 24             	mov    %eax,(%esp)
     d78:	e8 d3 fa ff ff       	call   850 <atoi@plt>
     d7d:	89 44 24 28          	mov    %eax,0x28(%esp)
     d81:	81 7c 24 28 ff 03 00 	cmpl   $0x3ff,0x28(%esp)
     d88:	00
     d89:	7f 1a                	jg     da5 <main+0xcd>
     d8b:	8d 83 37 e1 ff ff    	lea    -0x1ec9(%ebx),%eax
     d91:	89 04 24             	mov    %eax,(%esp)
     d94:	e8 07 fa ff ff       	call   7a0 <puts@plt>
     d99:	c7 04 24 01 00 00 00 	movl   $0x1,(%esp)
     da0:	e8 2b fa ff ff       	call   7d0 <exit@plt>
     da5:	c7 44 24 08 00 00 00 	movl   $0x0,0x8(%esp)
     dac:	00
     dad:	c7 44 24 04 01 00 00 	movl   $0x1,0x4(%esp)
     db4:	00
     db5:	c7 04 24 0a 00 00 00 	movl   $0xa,(%esp)
     dbc:	e8 9f fa ff ff       	call   860 <socket@plt>
     dc1:	89 44 24 2c          	mov    %eax,0x2c(%esp)
     dc5:	83 7c 24 2c ff       	cmpl   $0xffffffff,0x2c(%esp)
     dca:	75 1a                	jne    de6 <main+0x10e>
     dcc:	8d 83 54 e1 ff ff    	lea    -0x1eac(%ebx),%eax
     dd2:	89 04 24             	mov    %eax,(%esp)
     dd5:	e8 a6 f9 ff ff       	call   780 <perror@plt>
     dda:	c7 04 24 01 00 00 00 	movl   $0x1,(%esp)
     de1:	e8 ea f9 ff ff       	call   7d0 <exit@plt>
     de6:	8d 83 65 e1 ff ff    	lea    -0x1e9b(%ebx),%eax
     dec:	89 04 24             	mov    %eax,(%esp)
     def:	e8 ac f9 ff ff       	call   7a0 <puts@plt>
     df4:	c7 44 24 08 1c 00 00 	movl   $0x1c,0x8(%esp)
     dfb:	00
     dfc:	c7 44 24 04 00 00 00 	movl   $0x0,0x4(%esp)
     e03:	00
     e04:	8d 44 24 34          	lea    0x34(%esp),%eax
     e08:	89 04 24             	mov    %eax,(%esp)
     e0b:	e8 00 fa ff ff       	call   810 <memset@plt>
     e10:	66 c7 44 24 34 0a 00 	movw   $0xa,0x34(%esp)
     e17:	8b 83 6c 00 00 00    	mov    0x6c(%ebx),%eax
     e1d:	8b 10                	mov    (%eax),%edx
     e1f:	89 54 24 3c          	mov    %edx,0x3c(%esp)
     e23:	8b 50 04             	mov    0x4(%eax),%edx
     e26:	89 54 24 40          	mov    %edx,0x40(%esp)
     e2a:	8b 50 08             	mov    0x8(%eax),%edx
     e2d:	89 54 24 44          	mov    %edx,0x44(%esp)
     e31:	8b 40 0c             	mov    0xc(%eax),%eax
     e34:	89 44 24 48          	mov    %eax,0x48(%esp)
     e38:	8b 44 24 28          	mov    0x28(%esp),%eax
     e3c:	0f b7 c0             	movzwl %ax,%eax
     e3f:	89 04 24             	mov    %eax,(%esp)
     e42:	e8 19 f9 ff ff       	call   760 <htons@plt>
     e47:	66 89 44 24 36       	mov    %ax,0x36(%esp)
     e4c:	c7 44 24 10 04 00 00 	movl   $0x4,0x10(%esp)
     e53:	00
     e54:	8d 44 24 20          	lea    0x20(%esp),%eax
     e58:	89 44 24 0c          	mov    %eax,0xc(%esp)
     e5c:	c7 44 24 08 02 00 00 	movl   $0x2,0x8(%esp)
     e63:	00
     e64:	c7 44 24 04 01 00 00 	movl   $0x1,0x4(%esp)
     e6b:	00
     e6c:	8b 44 24 2c          	mov    0x2c(%esp),%eax
     e70:	89 04 24             	mov    %eax,(%esp)
     e73:	e8 b8 f8 ff ff       	call   730 <setsockopt@plt>
     e78:	85 c0                	test   %eax,%eax
     e7a:	79 0e                	jns    e8a <main+0x1b2>
     e7c:	8d 83 74 e1 ff ff    	lea    -0x1e8c(%ebx),%eax
     e82:	89 04 24             	mov    %eax,(%esp)
     e85:	e8 f6 f8 ff ff       	call   780 <perror@plt>
     e8a:	c7 44 24 08 1c 00 00 	movl   $0x1c,0x8(%esp)
     e91:	00
     e92:	8d 44 24 34          	lea    0x34(%esp),%eax
     e96:	89 44 24 04          	mov    %eax,0x4(%esp)
     e9a:	8b 44 24 2c          	mov    0x2c(%esp),%eax
     e9e:	89 04 24             	mov    %eax,(%esp)
     ea1:	e8 5a f9 ff ff       	call   800 <bind@plt>
     ea6:	83 f8 ff             	cmp    $0xffffffff,%eax
     ea9:	75 1a                	jne    ec5 <main+0x1ed>
     eab:	8d 83 89 e1 ff ff    	lea    -0x1e77(%ebx),%eax
     eb1:	89 04 24             	mov    %eax,(%esp)
     eb4:	e8 c7 f8 ff ff       	call   780 <perror@plt>
     eb9:	c7 04 24 01 00 00 00 	movl   $0x1,(%esp)
     ec0:	e8 0b f9 ff ff       	call   7d0 <exit@plt>
     ec5:	c7 44 24 04 05 00 00 	movl   $0x5,0x4(%esp)
     ecc:	00
     ecd:	8b 44 24 2c          	mov    0x2c(%esp),%eax
     ed1:	89 04 24             	mov    %eax,(%esp)
     ed4:	e8 67 f9 ff ff       	call   840 <listen@plt>
     ed9:	83 f8 ff             	cmp    $0xffffffff,%eax
     edc:	75 1a                	jne    ef8 <main+0x220>
     ede:	8d 83 98 e1 ff ff    	lea    -0x1e68(%ebx),%eax
     ee4:	89 04 24             	mov    %eax,(%esp)
     ee7:	e8 94 f8 ff ff       	call   780 <perror@plt>
     eec:	c7 04 24 01 00 00 00 	movl   $0x1,(%esp)
     ef3:	e8 d8 f8 ff ff       	call   7d0 <exit@plt>
     ef8:	8b 44 24 28          	mov    0x28(%esp),%eax
     efc:	89 44 24 04          	mov    %eax,0x4(%esp)
     f00:	8d 83 a9 e1 ff ff    	lea    -0x1e57(%ebx),%eax
     f06:	89 04 24             	mov    %eax,(%esp)
     f09:	e8 32 f8 ff ff       	call   740 <printf@plt>
     f0e:	c7 44 24 24 1c 00 00 	movl   $0x1c,0x24(%esp)
     f15:	00
     f16:	8d 44 24 24          	lea    0x24(%esp),%eax
     f1a:	89 44 24 08          	mov    %eax,0x8(%esp)
     f1e:	8d 44 24 50          	lea    0x50(%esp),%eax
     f22:	89 44 24 04          	mov    %eax,0x4(%esp)
     f26:	8b 44 24 2c          	mov    0x2c(%esp),%eax
     f2a:	89 04 24             	mov    %eax,(%esp)
     f2d:	e8 5e f8 ff ff       	call   790 <accept@plt>
     f32:	89 44 24 30          	mov    %eax,0x30(%esp)
     f36:	83 7c 24 30 ff       	cmpl   $0xffffffff,0x30(%esp)
     f3b:	75 11                	jne    f4e <main+0x276>
     f3d:	8d 83 c4 e1 ff ff    	lea    -0x1e3c(%ebx),%eax
     f43:	89 04 24             	mov    %eax,(%esp)
     f46:	e8 35 f8 ff ff       	call   780 <perror@plt>
     f4b:	90                   	nop
     f4c:	eb c0                	jmp    f0e <main+0x236>
     f4e:	8d 83 d5 e1 ff ff    	lea    -0x1e2b(%ebx),%eax
     f54:	89 04 24             	mov    %eax,(%esp)
     f57:	e8 44 f8 ff ff       	call   7a0 <puts@plt>
     f5c:	e8 cf f8 ff ff       	call   830 <fork@plt>
     f61:	83 f8 ff             	cmp    $0xffffffff,%eax
     f64:	74 06                	je     f6c <main+0x294>
     f66:	85 c0                	test   %eax,%eax
     f68:	74 12                	je     f7c <main+0x2a4>
     f6a:	eb 28                	jmp    f94 <main+0x2bc>
     f6c:	8d 83 e5 e1 ff ff    	lea    -0x1e1b(%ebx),%eax
     f72:	89 04 24             	mov    %eax,(%esp)
     f75:	e8 06 f8 ff ff       	call   780 <perror@plt>
     f7a:	eb 18                	jmp    f94 <main+0x2bc>
     f7c:	8b 44 24 30          	mov    0x30(%esp),%eax
     f80:	89 04 24             	mov    %eax,(%esp)
     f83:	e8 a3 fb ff ff       	call   b2b <handle_client>
     f88:	c7 04 24 00 00 00 00 	movl   $0x0,(%esp)
     f8f:	e8 3c f8 ff ff       	call   7d0 <exit@plt>
     f94:	8b 44 24 30          	mov    0x30(%esp),%eax
     f98:	89 04 24             	mov    %eax,(%esp)
     f9b:	e8 e0 f8 ff ff       	call   880 <close@plt>
     fa0:	e9 69 ff ff ff       	jmp    f0e <main+0x236>
     fa5:	66 90                	xchg   %ax,%ax
     fa7:	66 90                	xchg   %ax,%ax
     fa9:	66 90                	xchg   %ax,%ax
     fab:	66 90                	xchg   %ax,%ax
     fad:	66 90                	xchg   %ax,%ax
     faf:	90                   	nop
