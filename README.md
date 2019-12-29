# TipeData_Set__PY

Bahan Ajar Fundamental Pemrograman Python. Mengenal Dan Menggunakan Tipe Data Set Pada Pemrograman Python.<br><br>
<img src="https://github.com/RizkyKhapidsyah/TipeData_Set__PY/blob/master/result/001.PNG"><br><br>
- Lihat <a href="https://github.com/RizkyKhapidsyah/TipeData_Set__PY/blob/master/TipeData_Set__PY.py">Source Code</a><br><br>

-----

Tipe data Set Python adalah tipe data yang berisi kumpulan tipe data dan dipakai untuk mengolah himpunan (set). Jika dibandingkan dengan tipe data berbentuk array lain di Python, tipe data set berbeda dalam hal index, pengurutan dan keunikan nilai (unique value). 

Tipe data set tidak memiliki index, sehingga tidak ada mekanisme pengurutan. Maksudnya, ketika kita menginput beberapa nilai ke dalam tipe data set, posisi nilai tersebut bisa berada di mana saja, tidak persis seperti apa yang tertulis. Akibat tidak memiliki index, maka kita tidak bisa menambah nilai baru ke dalam tipe data set dengan cara menulis nomor index (seperti di dalam tipe data list)

Ciri khas selanjutnya dari tipe data set adalah tidak bisa menerima nilai ganda, setiap nilai di dalam set harus unik. Jika kita menginput beberapa nilai yang sama, hanya satu yang tersimpan di dalam set.Untuk memahami lebih lanjut pengertian tipe data set Python ini, kita akan bahas dengan contoh kode program.

Note: Selain Python, bahasa pemrograman lain yang juga memiliki tipe data set adalah Pascal: Pengertian dan Cara Penggunaan Tipe Data Set Pascal.

# Cara Pembuatan Tipe Data Set Python

Untuk membuat tipe data set, gunakan tanda kurung kurawal, kemudian setiap anggota set dipisah dengan tanda koma. Berikut contohnya:

      foo = {"Belajar", "Python", "di", "rikymetalist.blogspot.com"}
      bar = {100, 200, 300, 400}
      baz = {"Python", 200, 6.99, True}

      print(foo)
      print(bar)
      print(baz)

Selain perbedaan tanda kurung, cara penulisan tipe data set tidak berbeda dengan tipe data list dan tuple yang sudah kita pelajari sebelum ini. Perhatikan urutan data yang tampil, hampir semuanya tidak terurut sesuai penulisan. Ini karena di dalam tipe data set setiap anggota atau element tidak memiliki index sehingga posisinya tidak bisa dipastikan. Menggunakan function <code>type()</code>, kita bisa melihat perbedaan cara penulisan tipe data list, tuple dan set dalam bahasa Python:

      foo = ["Belajar", "Python", "di", "rikymetalist.blogspot.com"]
      print(type(foo))

      foo = ("Belajar", "Python", "di", "rikymetalist.blogspot.com")
      print(type(foo))

      foo = {"Belajar", "Python", "di", "rikymetalist.blogspot.com"}
      print(type(foo))

Pada kode program diatas, baris 1 adalah cara pembuatan tipe data list, baris 4 pembuatan tipe data tuple, dan baris 7 adalah cara pembuatan tipe data set.

# Sifat Tipe Data Set Python

Seperti yang dibahas pada bagian pengertian, sifat dari tipe data set adalah tidak ber-index dan hanya bisa menerima anggota dengan nilai yang berbeda (unique value). Mari lihat dengan contoh kode program:

      foo = {"Belajar", "Python", "di", "rikymetalist.blogspot.com", "di"}
      bar = {100, 200, 300, 400, 200, 300}

      print(foo)
      print(bar)


Untuk variabel <code>foo</code> saya menginput string “di” sebanyak 2 kali namun yang masuk hanya 1 buah. Begitu pula untuk variabel bar yang saya input dua kali nilai 200 dan 300 (total 6 element). Namun yang ditampung hanya 4 element saja dimana angka 200 dan 300 muncul hanya 1 kali. Selain itu tidak ada urutan yang pasti dari tipe data set. Bagaimana jika kita tetap mengakses anggota set menggunakan index? berikut hasilnya:

      foo = {"Belajar", "Python", "di", "rikymetalist.blogspot.com", "di"}
      print(foo[1]) # Akan Error


# Operasi Himpunan tipe data Set Python

Tipe data set pada dasarnya adalah tipe data khusus yang dipakai untuk operasi himpunan, seperti operasi gabungan (union), operasi irisan (intersection), dst. Lebih rinci tentang operasi himpunan ini akan kita bahas dalam tutorial khusus tenang operator di dalam bahasa Python. Namun sebagai gambaran, berikut contoh penggunaan tipe data set untuk operasi himpunan:

      foo = {1, 2, 3, 4, 5}
      bar = {3, 4, 5, 6, 7}

      print (foo | bar) # union
      print (foo & bar) # intersection

Dalam contoh di atas, perintah <code>foo</code> | <code>bar</code> adalah operasi gabungan himpunan. Hasilnya, seluruh anggota himpunan yang ada di variabel <code>foo</code> digabung dengan seluruh anggota dalam variabel <code>bar</code>, anggota yang ada di kedua himpunan hanya akan ditampilkan 1 kali. Perintah <code>foo</code> & <code>bar</code> adalah operasi irisan himpunan. Hasilnya adalah seluruh anggota yang terdapat di variabel <code>foo</code> dan juga ada di variabel <code>bar</code> (harus ada di kedua variabel).

-----

# Set

Set adalah salah satu tipe data di Python yang tidak berurut (unordered). Set memiliki anggota yang unik (tidak ada duplikasi). Jadi misalnya kalau kita meletakkan dua anggota yang sama di dalam set, maka otomatis set akan menghilangkan yang salah satunya. Set bisa digunakan untuk melakukan operasi himpunan matematika seperti gabungan, irisan, selisih, dan lain – lain.

# Membuat Set

Set dibuat dengan meletakkan anggota – anggotanya di dalam tanda kurung kurawal <code>{ }</code>, dipisahkan menggunakan tanda koma. Kita juga bisa membuat set dari list dengan memasukkan list ke dalam fungsi <code>set()</code>. Set bisa berisi data campuran, baik integer, float, string, dan lain sebagainya. Akan tetapi set tidak bisa berisi list, set, dan dictionary.

Untuk membuat set kosong, kita tidak bisa menggunakan { }, karena itu akan dianggap sebagai dictionary. Kita harus menggunakan fungsi set() tanpa argumen untuk membuat set kosong.

<pre>&gt;&gt;&gt; # membuat variabel a dengan {}
&gt;&gt;&gt; a = {}
&gt;&gt;&gt; print(type(a))
&lt;class 'dict'&gt;

&gt;&gt;&gt; # harus menggunakan fungsi set()
&gt;&gt;&gt; a = set()
&gt;&gt;&gt; print(type(a))
&lt;class 'set'&gt;

</pre>

# Mengubah Anggota Set

Set bersifat mutable. Tapi, karena set adalah tipe data tidak berurut (unordered), maka kita tidak bisa menggunakan indeks. Set tidak mendukung indeks ataupun slicing. Untuk menambah satu anggota ke dalam set, kita bisa menggunakan fungsi add(), dan untuk menambahkan beberapa anggota sekaligus kita bisa menggunakan fungsi <code>update()</code>. List, tuple, maupun string bisa digunakan sebagai masukan dari fungsi <code>update()</code>.

# Menghapus Anggota Set

Kita bisa menghapus anggota set dengan menggunakan fungsi <code>discard()</code> dan <code>remove()</code>. Perbedaannya, fungsi <code>discard()</code> tidak akan memunculkan error bila anggota yang ingin dihapus ternyata tidak ada di dalam set, sedangkan <code>remove()</code> sebaliknya.

Selain <code>discard()</code> dan <code>remove()</code>, kita bisa menghapus anggota set dengan menggunakan fungsi <code>pop()</code>. Dengan menggunakan fungsi pop(), kita menghapus salah satu anggota secara acak (random).

Untuk mengosongkan atau menghapus seluruh anggota set, kita bisa menggunakan fungsi <code>clear()</code>.
Set dapat digunakan untuk melakukan operasi himpunan matematika seperti gabungan, irisan, selisih, dan komplemen.

Mari kita ambil dua contoh set berikut:

      >>> A = {1, 2, 3, 4, 5}
      >>> B = {4, 5, 6, 7, 8}

# Operasi Gabungan (Union)

Gabungan (union) dari A dan B adalah himpunan atau set anggota yang ada di  A dan B. Gabungan dapat dibuat dengan menggunakan operator palang (|). Selain itu juga bisa dilakukan dengan menggunakan fungsi <code>union()</code>. Irisan (intersection) dari A dan B adalah himpunan atau set anggota yang sama di A dan B. Irisan dilakukan dengan menggunakan operator jangkar (&). Irisan juga bisa dilakukan dengan menggunakan fungsi <code>intersection()</code>.

# Operasi Selisih (Difference)

Selisih (intersection) dari A dan B adalah himpunan atau set anggota yang hanya ada di A dan tidak ada di B. Begitu juga sebaliknya, ada di B tapi tidak ada di A. Selisih dilakukan dengan menggunakan operator kurang <code>(-)</code>. Bisa juga dengan menggunakan fungsi <code>difference()</code>.

Operasi komplemen (symmetric difference) dari A dan B adalah himpunan atau set anggota yang ada di A dan di B, tapi tidak di keduanya. Komplemen dilakukan dengan menggunakan operator <code>^</code>. Bisa juga dengan menggunakan fungsi <code>symmetric_difference()</code>.

# Metode (Fungsi) Set

Set memiliki banyak metode atau fungsi. Beberapa di antaranya adalah yang sudah kita gunakan di atas. Tabel berikut berisi daftar metode atau fungsi set yang disediakan oleh python.

<table>
<tbody>
<tr>
<td><strong>Metode</strong></td>
<td><strong>Deskripsi</strong></td>
</tr>
<tr>
<td><span style="color: #800080;">add()</span></td>
<td>Menambahkan satu anggota ke set</td>
</tr>
<tr>
<td><span style="color: #800080;">clear()</span></td>
<td>Menghapus semua anggota set</td>
</tr>
<tr>
<td><span style="color: #800080;">copy()</span></td>
<td>Mengembalikan <em>shallow copy</em> dari set</td>
</tr>
<tr>
<td><span style="color: #800080;">difference()</span></td>
<td>Mengembalikan set baru berisi selisih dua atau lebih set</td>
</tr>
<tr>
<td><span style="color: #800080;">difference_update()</span></td>
<td>Menghapus semua anggota set lain yang ada di set ini</td>
</tr>
<tr>
<td><span style="color: #800080;">discard()</span></td>
<td>Menghapus satu anggota dari set</td>
</tr>
<tr>
<td><span style="color: #800080;">intersection()</span></td>
<td>Mengembalikan set baru berisi irisan antara dua atau lebih set</td>
</tr>
<tr>
<td><span style="color: #800080;">intersection_update()</span></td>
<td>Mengupdate set dengan irisan set bersangkutan dan set lainnya</td>
</tr>
<tr>
<td><span style="color: #800080;">isdisjoint()</span></td>
<td>Mengembalikan True jika dua set tidak memiliki irisan</td>
</tr>
<tr>
<td><span style="color: #800080;">issubset()</span></td>
<td>Mengembalikan True jika set lain berisi set ini</td>
</tr>
<tr>
<td><span style="color: #800080;">issuperset()</span></td>
<td>Mengembalikan True jika set ini berisi set lain</td>
</tr>
<tr>
<td><span style="color: #800080;">pop()</span></td>
<td>Menghapus dan mengembalikan anggota acak dari sebuah set</td>
</tr>
<tr>
<td><span style="color: #800080;">remove()</span></td>
<td>Menghapus satu anggota dari set</td>
</tr>
<tr>
<td><span style="color: #800080;">symmetric_difference()</span></td>
<td>Mengembalikan set baru berisi komplemen dari dua set</td>
</tr>
<tr>
<td><span style="color: #800080;">symmetric_difference_update()</span></td>
<td>Mengupdate set dengan komplemen dari set ini dan set lainnya</td>
</tr>
<tr>
<td><span style="color: #800080;">union()</span></td>
<td>Mengembalikan set baru berisi gabungan dua atau lebih set</td>
</tr>
<tr>
<td><span style="color: #800080;">update()</span></td>
<td>Mengupdate set dengan gabungan set ini dan set lainnya</td>
</tr>
</tbody>
</table>

-----
Referensi Artikel: <a href="https://www.duniailkom.com">DuniaIlkom</a>, <a href="https://www.pythonindo.com">PythonIndo</a>. Thanks to: <a href="https://www.duniailkom.com">DuniaIlkom</a>, <a href="https://www.pythonindo.com">PythonIndo</a><br>
Referensi Source Code: <a href="https://www.youtube.com/user/faqihzamukhlish"> Kelas Terbuka </a> dan <a href="https://github.com/kelasterbuka"> Kelas Terbuka (Repository)</a>. Created by <a href="https://github.com/faqihza">Faqihza Mukhlish.</a> Thanks To: <a href="https://www.youtube.com/channel/UCRGHjysoCemh4y7tCJQs30w/about">Faqihza Mukhlish.</a><br>

-----
All Source Code is Modified.
