int main() {
    string line = Stdio.stdin->gets();
    sscanf(line, "%d", int a);
    a *= 860798509;
    a += 198609463;
    a %= 1000000007;
    write(a+"\n");
    return 0;
}
