Uses FGInt, FGIntRSA;

Var
	p,q,N,phi,e,d : TFGInt;
	test, res, final : String;
begin
	Base10StringToFGInt('1148999747821254709185188541405920213718593747', p);
	Base10StringToFGInt('1329291547371927626651593780682612531815487963', q);
	FGIntMul(p, q, N);

	p.Number[1] := p.Number[1] - 1;
	q.Number[1] := q.Number[1] - 1;

	FGIntMul(p, q, phi);
	Base10StringToFGInt('65537', e);

	FGIntModInv(e, phi, d);

	test := 'NC';
	RSAEncrypt(test, d, N, res);
	//RSADecrypt("NC", d, N, Nilgint, Nilgint, Nilgint, Nilgint, res);
	ConvertBase256to64(res, final);
end.