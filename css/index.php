<html>
  <head>
    <title>
      Rea's erste Website
    </title>
    <link rel="stylesheet" type="text/css" href="style/style.css" />

  </head>

  <body>

        7 + 6 = 7<br>
<p>
        <?php
            $zahl1 = 7;
            $zahl2 = 6;
            $ergebnis = $zahl1 + $zahl2;
            echo "Ergebnis: $ergebnis";
        ?>


<div>
  <br>
  Hallo Welt
  <br>
</div>

<p><b><a href="www.google.com" target="_blank">Link zu Google</a></b></p>

<ul>
  <li><a href="#home">Home</a></li>
  <li><a href="#news">News</a></li>
  <li><a href="#contact">Contact</a></li>
  <li><a href="#about">About</a></li>
</ul>



<style>
.dropdown {
  position: relative;
  display: inline-block;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  padding: 12px 16px;
  z-index: 1;
}

.dropdown:hover .dropdown-content {
  display: block;
}
</style>

<div class="dropdown">
  <span>Mouse over me</span>
  <div class="dropdown-content">
    <p>Hello World!</p>
  </div>
</div> 







</body>
</html> 