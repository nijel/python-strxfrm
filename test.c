#include <locale.h>
#include <string.h>
#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>
#include <wchar.h>

int main(int argc, char** argv) {
    wchar_t *buf;
    size_t len;
    wchar_t string[] = L"š";

    buf = malloc(sizeof(wchar_t) * 40);

    printf("setlocale=%s\n", setlocale(LC_ALL, "en_US.UTF-8"));

    printf("wcsxfrm(1)=%zd\n", wcsxfrm(buf, string, 1));
    printf("wcsxfrm(40)=%zd\n", wcsxfrm(buf, string, 40));
    printf("buf=%ls\n", buf);
}
