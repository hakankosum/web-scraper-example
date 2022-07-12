var $table = $("#asd");
$table.find("th").each(function(columnIndex)
{
    var oldValue=0, currentValue=0, $elementToMark;
    var $trs = $table.find("tr");
    $trs.each(function(index, element)
    {
        oldValue= currentValue;
        var $td = $(this).find("td:eq("+ columnIndex +")");
        if ($td.length!=0)
        {
            currentValue= parseFloat($td.html());
            if(currentValue > oldValue)
            {
                $elementToMark= $td;
            }
            if(index == $trs.length-1)
            {
              $elementToMark.addClass("bg-primary");
            }
        }
    });
});