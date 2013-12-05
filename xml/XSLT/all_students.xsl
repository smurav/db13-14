<?xml version="1.0" encoding="ISO-8859-1"?>
<!-- Edited by XMLSpy® -->
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
  <body>
  <h2>Все студенты факультета КиБ</h2>
    <table border="1">
      <tr bgcolor="#9acd32">
        <th>Group_year</th>
        <th>Student</th>
        <th>Student</th>
      </tr>
      <xsl:for-each select="//department[../../@name='Кибернетика и Безопасность']">
      <xsl:for-each select="group/student">
      <tr>
        <td><xsl:value-of select="../@entry_year"/></td>
        <td><xsl:number/></td>
        <td><xsl:value-of select="@name"/></td>
      </tr>
      </xsl:for-each>
      </xsl:for-each>
    </table>
  </body>
  </html>
</xsl:template>
</xsl:stylesheet>


