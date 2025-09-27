import hashlib  # hashlib 모듈을 import하여 SHA1 해시 생성 (Python 공식 문서 기반)

# startNum과 endNum을 설정 (예: 1부터 5까지)
startNum = 1  # 시작 숫자 설정
endNum = 200    # 끝 숫자 설정

s1 = set()

# startNum부터 endNum까지 루프를 돌며 각 숫자를 SHA1 해시로 변환하고 출력
for num in range(startNum, endNum + 1):  # range 함수로 숫자 범위 생성 (Python 기본 기능)
    # 숫자를 문자열로 변환하여 해시 계산 (SHA1은 바이트 입력 필요)
    hash_obj = hashlib.sha1(str(num).encode())  # SHA1 해시 객체 생성 및 업데이트
    hash_value = hash_obj.hexdigest()  # 16진수 문자열로 해시 값 얻기 (길이: 40자리, 160비트)
    # 숫자와 해시를 출력 (요청대로 숫자와 해시 모두 출력)
    # print(f"Number: {num}, SHA1 Hash: {hash_value}")  # 출력 형식: 숫자와 해시
    print(f"Number: {num}, SHA1 Hash: {hash_value[:6]}")  # 출력 형식: 숫자와 해시
    s1.add(hash_value[:6])

# 총 고유 해시 개수 출력 - 해시 검증
print(f'Total unique hashes (first 6 chars): {len(s1)}')

'''
Number: 1, SHA1 Hash: 356a19
Number: 2, SHA1 Hash: da4b92
Number: 3, SHA1 Hash: 77de68
Number: 4, SHA1 Hash: 1b6453
Number: 5, SHA1 Hash: ac3478
Number: 6, SHA1 Hash: c1dfd9
Number: 7, SHA1 Hash: 902ba3
Number: 8, SHA1 Hash: fe5dbb
Number: 9, SHA1 Hash: 0ade7c
Number: 10, SHA1 Hash: b1d578
Number: 11, SHA1 Hash: 17ba07
Number: 12, SHA1 Hash: 7b5200
Number: 13, SHA1 Hash: bd307a
Number: 14, SHA1 Hash: fa35e1
Number: 15, SHA1 Hash: f1abd6
Number: 16, SHA1 Hash: 1574bd
Number: 17, SHA1 Hash: 0716d9
Number: 18, SHA1 Hash: 9e6a55
Number: 19, SHA1 Hash: b3f0c7
Number: 20, SHA1 Hash: 91032a
Number: 21, SHA1 Hash: 472b07
Number: 22, SHA1 Hash: 12c6fc
Number: 23, SHA1 Hash: d435a6
Number: 24, SHA1 Hash: 4d134b
Number: 25, SHA1 Hash: f6e112
Number: 26, SHA1 Hash: 887309
Number: 27, SHA1 Hash: bc33ea
Number: 28, SHA1 Hash: 0a57cb
Number: 29, SHA1 Hash: 7719a1
Number: 30, SHA1 Hash: 22d200
Number: 31, SHA1 Hash: 632667
Number: 32, SHA1 Hash: cb4e52
Number: 33, SHA1 Hash: b6692e
Number: 34, SHA1 Hash: f1f836
Number: 35, SHA1 Hash: 972a67
Number: 36, SHA1 Hash: fc074d
Number: 37, SHA1 Hash: cb7a1d
Number: 38, SHA1 Hash: 5b384c
Number: 39, SHA1 Hash: ca3512
Number: 40, SHA1 Hash: af3e13
Number: 41, SHA1 Hash: 761f22
Number: 42, SHA1 Hash: 92cfce
Number: 43, SHA1 Hash: 0286dd
Number: 44, SHA1 Hash: 98fbc4
Number: 45, SHA1 Hash: fb6443
Number: 46, SHA1 Hash: fe2ef4
Number: 47, SHA1 Hash: 827bfc
Number: 48, SHA1 Hash: 64e095
Number: 49, SHA1 Hash: 2e01e1
Number: 50, SHA1 Hash: e1822d
Number: 51, SHA1 Hash: b7eb6c
Number: 52, SHA1 Hash: a93349
Number: 53, SHA1 Hash: c5b76d
Number: 54, SHA1 Hash: 80e28a
Number: 55, SHA1 Hash: 8effee
Number: 56, SHA1 Hash: 54ceb9
Number: 57, SHA1 Hash: 9109c8
Number: 58, SHA1 Hash: 667be5
Number: 59, SHA1 Hash: 5a5b0f
Number: 60, SHA1 Hash: e6c3dd
Number: 61, SHA1 Hash: 6c1e67
Number: 62, SHA1 Hash: 511a41
Number: 63, SHA1 Hash: a17554
Number: 64, SHA1 Hash: c66c65
Number: 65, SHA1 Hash: 2a4593
Number: 66, SHA1 Hash: 59129a
Number: 67, SHA1 Hash: 4d89d2
Number: 68, SHA1 Hash: b4c96d
Number: 69, SHA1 Hash: a72b20
Number: 70, SHA1 Hash: b7103c
Number: 71, SHA1 Hash: d02560
Number: 72, SHA1 Hash: c09763
Number: 73, SHA1 Hash: 35e995
Number: 74, SHA1 Hash: 1f1362
Number: 75, SHA1 Hash: 450dde
Number: 76, SHA1 Hash: d54ad0
Number: 77, SHA1 Hash: d321d6
Number: 78, SHA1 Hash: eb4ac3
Number: 79, SHA1 Hash: b74f5e
Number: 80, SHA1 Hash: b888b2
Number: 81, SHA1 Hash: 1d513c
Number: 82, SHA1 Hash: 76546f
Number: 83, SHA1 Hash: 7d7116
Number: 84, SHA1 Hash: be461a
Number: 85, SHA1 Hash: 135224
Number: 86, SHA1 Hash: 3c26df
Number: 87, SHA1 Hash: e62d7f
Number: 88, SHA1 Hash: b37f6d
Number: 89, SHA1 Hash: 16b06b
Number: 90, SHA1 Hash: 2d0c8a
Number: 91, SHA1 Hash: 4cd66d
Number: 92, SHA1 Hash: 8ee51c
Number: 93, SHA1 Hash: 08a352
Number: 94, SHA1 Hash: 215bb4
Number: 95, SHA1 Hash: 8e63fd
Number: 96, SHA1 Hash: 6fb84a
Number: 97, SHA1 Hash: 812ed4
Number: 98, SHA1 Hash: 31bd9b
Number: 99, SHA1 Hash: 9a79be
Number: 100, SHA1 Hash: 310b86
Number: 101, SHA1 Hash: dbc0f0
Number: 102, SHA1 Hash: c8306a
Number: 103, SHA1 Hash: 934385
Number: 104, SHA1 Hash: 78a8ef
Number: 105, SHA1 Hash: e114c4
Number: 106, SHA1 Hash: 7224f9
Number: 107, SHA1 Hash: 524e05
Number: 108, SHA1 Hash: 17503a
Number: 109, SHA1 Hash: a1422e
Number: 110, SHA1 Hash: 5e796e
Number: 111, SHA1 Hash: 6216f8
Number: 112, SHA1 Hash: 601ca9
Number: 113, SHA1 Hash: e99321
Number: 114, SHA1 Hash: ecb793
Number: 115, SHA1 Hash: efa6e4
Number: 116, SHA1 Hash: 683e72
Number: 117, SHA1 Hash: d0e2db
Number: 118, SHA1 Hash: 12f0de
Number: 119, SHA1 Hash: a2e33d
Number: 120, SHA1 Hash: 775bc5
Number: 121, SHA1 Hash: 8bd795
Number: 122, SHA1 Hash: 05a8ea
Number: 123, SHA1 Hash: 40bd00
Number: 124, SHA1 Hash: f38cfe
Number: 125, SHA1 Hash: 0ca927
Number: 126, SHA1 Hash: 114d4e
Number: 127, SHA1 Hash: 008451
Number: 128, SHA1 Hash: b4182b
Number: 129, SHA1 Hash: 8b7471
Number: 130, SHA1 Hash: 2a7541
Number: 131, SHA1 Hash: e794a8
Number: 132, SHA1 Hash: 91dfde
Number: 133, SHA1 Hash: d30f79
Number: 134, SHA1 Hash: 95e815
Number: 135, SHA1 Hash: 40f7c0
Number: 136, SHA1 Hash: 9e071a
Number: 137, SHA1 Hash: e1a864
Number: 138, SHA1 Hash: 56ad4d
Number: 139, SHA1 Hash: fa7557
Number: 140, SHA1 Hash: c28aca
Number: 141, SHA1 Hash: c9ca44
Number: 142, SHA1 Hash: 2a2b47
Number: 143, SHA1 Hash: f47aea
Number: 144, SHA1 Hash: 732082
Number: 145, SHA1 Hash: 50336b
Number: 146, SHA1 Hash: 3fcfb9
Number: 147, SHA1 Hash: b3c073
Number: 148, SHA1 Hash: 536fb6
Number: 149, SHA1 Hash: 39dfc9
Number: 150, SHA1 Hash: 13682a
Number: 151, SHA1 Hash: b16a45
Number: 152, SHA1 Hash: ac2646
Number: 153, SHA1 Hash: a6f16a
Number: 154, SHA1 Hash: 06349b
Number: 155, SHA1 Hash: 9d8974
Number: 156, SHA1 Hash: 605252
Number: 157, SHA1 Hash: 097ccd
Number: 158, SHA1 Hash: a3d125
Number: 159, SHA1 Hash: 6b6277
Number: 160, SHA1 Hash: be057d
Number: 161, SHA1 Hash: 0159a9
Number: 162, SHA1 Hash: ae1e71
Number: 163, SHA1 Hash: fd9375
Number: 164, SHA1 Hash: a929eb
Number: 165, SHA1 Hash: 74cbd2
Number: 166, SHA1 Hash: 69e569
Number: 167, SHA1 Hash: 708a77
Number: 168, SHA1 Hash: f76b2e
Number: 169, SHA1 Hash: 2659fc
Number: 170, SHA1 Hash: 717b2f
Number: 171, SHA1 Hash: 94940e
Number: 172, SHA1 Hash: c1aa04
Number: 173, SHA1 Hash: 572e20
Number: 174, SHA1 Hash: d09470
Number: 175, SHA1 Hash: 04f124
Number: 176, SHA1 Hash: 5c8f5a
Number: 177, SHA1 Hash: 26e745
Number: 178, SHA1 Hash: 25293f
Number: 179, SHA1 Hash: 9e44d2
Number: 180, SHA1 Hash: ec7f1f
Number: 181, SHA1 Hash: aee544
Number: 182, SHA1 Hash: 58f074
Number: 183, SHA1 Hash: dc685e
Number: 184, SHA1 Hash: bcf814
Number: 185, SHA1 Hash: cfa2ed
Number: 186, SHA1 Hash: 87d538
Number: 187, SHA1 Hash: f67462
Number: 188, SHA1 Hash: acf1ff
Number: 189, SHA1 Hash: e54183
Number: 190, SHA1 Hash: 3a2dc6
Number: 191, SHA1 Hash: 2fcc82
Number: 192, SHA1 Hash: 19a448
Number: 193, SHA1 Hash: 14bb99
Number: 194, SHA1 Hash: 2a79f1
Number: 195, SHA1 Hash: 752ae7
Number: 196, SHA1 Hash: 4dea1d
Number: 197, SHA1 Hash: 61188f
Number: 198, SHA1 Hash: c83730
Number: 199, SHA1 Hash: 2952ae
Number: 200, SHA1 Hash: 9f9af0
'''