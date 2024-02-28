
Sub retrieveTickerSummary()
    Dim ticker_symbol As String
    Dim year_opening_val, year_closing_val, year_change As Double
    Dim year_change_percent As Double
    Dim summary_row_num As Integer
    Dim year_volume As LongLong
    Dim LastRowofA, LastRowofI As Long

    'Generating summary columns
    Cells(1, 9).Value = "<ticker symbol>"
    Cells(1, 10).Value = "<yr change>"
    Cells(1, 11).Value = "<percent change>"
    Cells(1, 12).Value = "<total vol>"
    
    summary_row_num = 2 ' Tracks row num in summary table
    LastRowofA = ActiveSheet.Cells(ActiveSheet.Rows.Count, "A").End(xlUp).Row ' Tracks last value of Col A
    
    For I = 2 To LastRowofA
        If Cells(I, 2).Value Like "*0102" Then ' Captures symbol's opening num at 1/1
            year_opening_val = Cells(I, 3).Value
            year_volume = Cells(I, 7).Value
        ElseIf Cells(I, 1).Value = Cells(I + 1, 1).Value Then ' Continues adding volume if like previous ticker
            year_volume = year_volume + Cells(I, 7).Value
        ElseIf Cells(I, 2).Value Like "*1231" Then
        'ElseIf Cells(i, 1).Value <> Cells(i + 1, 1).Value Then
            year_volume = year_volume + Cells(I, 7).Value ' Captures last volume num
            year_closing_val = Cells(I, 6).Value 'Captures year end closing val
            ticker_symbol = Cells(I, 1).Value ' Captures ticker sym
            year_change = year_closing_val - year_opening_val  'Calculate opening to ending val
            year_change_percent = ((year_closing_val / year_opening_val) - 1) ' Calculates % change
            ' Adding to summary table with formatting...
            Cells(summary_row_num, 9).Value = ticker_symbol
            Cells(summary_row_num, 10).Value = year_change
                If year_change < 0 Then
                    Cells(summary_row_num, 10).Interior.ColorIndex = 3
                ElseIf year_change_percent = 0 Then
                    Cells(summary_row_num, 10).Interior.ColorIndex = 2
                 Else
                     Cells(summary_row_num, 10).Interior.ColorIndex = 4
                End If
                Cells(summary_row_num, 10).NumberFormat = "$0.00"
            Cells(summary_row_num, 11).Value = year_change_percent
            Cells(summary_row_num, 11).NumberFormat = "0.00%"
            Cells(summary_row_num, 12).Value = year_volume
            summary_row_num = summary_row_num + 1
        Else
            MsgBox ("Data seems incomplete... check if all symbols have opening closing dates")
        End If
    Next I
End Sub

Sub retrieveYearlyWinnerLoserMover()
    Dim LastRowofI As Long
    Dim Winner_sym, Loser_sym, Mover_sym As String
    Dim Winner, Loser As Double
    Dim Mover As LongLong
    LastRowofI = ActiveSheet.Cells(ActiveSheet.Rows.Count, "I").End(xlUp).Row ' Tracks last value of Col I
    'Generating table...
    Cells(1, 15).Value = "<ticket sym>"
    Cells(1, 16).Value = "<value>"
    Cells(2, 14).Value = "Greatest % increase"
    Cells(3, 14).Value = "Greatest % decrease"
    Cells(4, 14).Value = "Greatest Volume"
    ' Ref first row summary
        'Winner = Cells(2, 11).Value
        'Loser = Cells(2, 11).Value
        'Mover = Cells(2, 12).Value
     ' Iterating through summary table:
        For I = 2 To LastRowofI
            'Grabbing winner
            If Cells(I, 11).Value > Winner Then
                Winner = Cells(I, 11).Value
                Winner_sym = Cells(I, 9).Value
            End If
            'Grabbing loser
            If Cells(I, 11).Value < Loser Then
                Loser = Cells(I, 11).Value
                Loser_sym = Cells(I, 9).Value
            End If
            'Grabbing mover
            If Cells(I, 12).Value > Mover Then
                Mover = Cells(I, 12).Value
                Mover_sym = Cells(I, 9).Value
            End If
        Next I
        'Assignment
    Cells(2, 15).Value = Winner_sym
    Cells(2, 16).Value = Winner
    Cells(2, 16).NumberFormat = "0.00 %"
    Cells(3, 15).Value = Loser_sym
    Cells(3, 16).Value = Loser
    Cells(3, 16).NumberFormat = "0.00 %"
    Cells(4, 15).Value = Mover_sym
    Cells(4, 16).Value = Mover
End Sub

Sub applyToAllSheets()
Dim ws As Worksheet
    For Each ws In Worksheets
        With ws
            .Select
             retrieveTickerSummary
             retrieveYearlyWinnerLoserMover
        End With
    Next ws
End Sub

Sub resetSheet()
    Worksheets("2018").Columns("I:P").ClearContents
    Worksheets("2018").Columns("I:P").ClearFormats
    Worksheets("2019").Columns("I:P").ClearContents
    Worksheets("2019").Columns("I:P").ClearFormats
    Worksheets("2020").Columns("I:P").ClearContents
    Worksheets("2020").Columns("I:P").ClearFormats
End Sub



