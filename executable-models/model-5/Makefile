# This does not work due to https://github.com/kenmcmil/ivy/issues/16
all: network.ivy node.ivy sort.ivy assertion.ivy executable.ivy
	ivy_to_cpp target=repl isolate=executable_runner executable.ivy
	g++ -O2 executable.cpp -pthread -lpthread -o executable

# This does not work due to https://github.com/kenmcmil/ivy/issues/16
fuzz: network.ivy node.ivy sort.ivy assertion.ivy fuzz.ivy
	ivyc target=test isolate=fuzz_runner classname=fuzz fuzz.ivy

proof: network.ivy node.m4.ivy sort.ivy assertion.ivy proof.m4.ivy
	m4 node.m4.ivy > node.ivy
	m4 proof.m4.ivy > proof.ivy
	ivy_check trace=true proof.ivy

format: relation.py
	autopep8 -i relation.py
