Wrote subtitles in Hebrew or Arabic and now want to fix the rtl issue in
the srt file? There are some sites like pixiesoft.com which allow to swap
the text, but they destroy the srt metadata.

This lazy script produces the pure text without the metadata, then allows to
merge it back in so we can use www.pixiesoft.com/flip/ and chosing RTL to LTR,
for example, to fix the punctuations issues and then merge the result back in.

TODO:
- Automize the rtl fix with urllib2
- Write rtl fix logic
