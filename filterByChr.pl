#filter out non autochromosomal or X,Y chrs
while(<>){
	chomp;
	my @tmps = split(/\t/);
	if($tmps[2] =~ /chr[0-9XY]+/){

	print "$_\n";
}else{
next;}
}
