
<?php   
    $nombre = $_POST['nombre'];
    $puesto = $_POST['puesto'];
    $salario = $_POST['salario'];

    $bono = 0;

    match ($puesto){
        "Gerente" => $bono = $salario * 0.20, 
        "Supervisor" => $bono = $salario + 0.15, 
        "Cajero" =>  $bono = $salario * 0.10, 
        "Vendedor" => $bono = $salario * 0.08,
        default => $bono = "Ingrese un puesto válido"


    }

?>

<table>
    <tr>
        <th>Nombre del empleado</th>
        <th>Puesto administrativo</th>
        <th>Salario Designado</th>
        <th>Bonificacion</th>
    </tr>
    <tr>
        <td><?php echo $nombre ?></td>
        <td><?php echo $puesto ?></td>
        <td><?php echo $salario ?></td>
        <td><?php echo $bono ?></td>

    </tr>
</table>