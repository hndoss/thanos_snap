def print_thanos_banner_before_snap():
    print("""
                                                              `.--..``                                                                                    
                                                       .:/+oooo+++/:-.                                                                                
                                                    .-/++ooosooo++++//:.                                                                              
                                                   --:/+ossssosso+/+//::.                                                                             
                                                  `..-:osyyssssooo///::::`                                                                            
                                                  .-.-/syyyysssso+++/:::/.                                                                            
                                                  `:--:oyyysyyssso+//::/::                                                                            
                                                  `-:-+shhysyyyyyss++/:/:/+o`                                                                         
                                                  .::sydddddhhddmmdhso+/:/sh:                                                                         
                                                 `y::hddNmNmhsydddhysso/::+y:                                                                         
                                                  y+:+syhhdoysosyyssso+/::/+.                 `                                                       
                                                  /++/+yyhdhmdyhyhhys+::::/+:`              `/oo/--`                                                  
                                                  -o//shdddhhdhyysyhho/////:ys-          ./sshddddyo.                                                 
                                                   `:+ymmhydddddhhydhh///o+:so::-`    `/yydmdmmddyyyho-..:++/`                                        
                                                    /o+ddhohdddhhysydds++ooss`.-:/:.-:oddddddmmddhhddyysyddhyso/:/-                                   
                                                    -sohysyhmdmddhsyshhsoooh-.`/ooy+ydhmdmddddmdhdhssyhhhsyhdhshooo::-`                               
                                                    `+oyyyhhdddddhyyysyysyh+:-:oysdddmmmdddmmmddhhys+++ohdydsydssooo+/.                               
                                                     +ysyyhhhdddddhyyyhydmdooo+sy+ommmmmmdhmmdddhhd+oo+/ohhyddhdo+sss/`                               
                                                   .:sdsdhdddmmNmmmdmdmdddNyyy/hddhmyoydmdhddmmddhyshy++/oyyyddhdo:/s..                               
                                                `-/+symshhddNNNNNNNNNmdhhdmmy/ooymmmmdddmdmddhhyssssoys+o:ooyyhdysso/``                               
                                              `-/+osyhdmydyhdmmNNNNmmdddhhdNdoohddmmmmmmmmmdho:+++-://o+o+:+oyddh/ds` `                               
                                            `-+++oshhhymhhdhhdmmmmddddddhhdmNdmhhyosddmmmmmdy/-/o::./+ssoss:oshdm++y//:-``                            
                                         `.:/s++oshhhhydNhdmddmmmmmmddddhddmddmmdhyhddddddmhhs/:+/:/s+yyss+o+oydm/:o//+/:-.`                          
                                      `-/+/:o++oyhhhddhmMmhmmmmNmmmmddddhhdmmmmNNddmmmddhyddhddyyyyysyhhyso/+:shhyhy+:++/:::.                         
                                   `-/+++:--h+syhhddyyoNMNhdddddmmmddddddmmNmdmmNmddddmmmmdddmmmmdmddmdhdhyho-/yso+/:o+o/::-:.                        
                                 .:/+++s/..ohsyyhdys+o+mmdhdddhhhddhhddmmmmddddmmmNddddmmmmdmmdmddmmhdmddddyh+/sydh+:/oo+/:---`                       
                                .:://oys.``hyyyhyyss+s+sddhhhhhhhhhhddmmdhhdhdddmmmmmddmmmmmmmdddmNddhhmddhhysssyhmNh:o+//:----                       
                               .:/::+sh. `///yyysssossyhhhyyddhhhhdmdhhyhhhhhhddhhdmmmNmmmmmmmmdmdmmmmdhhyysoyyyhhddmmmdsoy+---.                      
                              .:/::/oho``+.-yy+ysoyoshhhyyyyhdhhddyhyyyyssssyhhdhdmmmmNMMNmmmmddmmmmmdddysshhssyhhhdddmddy/oso:-                      
                             -::+//oyd:` /.yos+soosssyhhhhyshmmmddossoosyhhyyhhhddmmNNNMMNMNNmmmddmmmmdddmdydhhdyhsdmmmydhs/::os/-                    
                             /:+++oydmh. :+yoo++ooossooosyysymNmddyo+syyyyyyhhhdmmNNNNNNNNNNMNmmdhdmmmmmmmddhsshysyoyhhhdhys+:..oyo:-                 
                             /+oyoyhdmms:dho+syyyssyhhyysosshmmmdhssyyyssyyyhddmNNNNNNNNNNNNNNmyyhmhdmNNNmdmhysshsossyhhyyhhso/-`-syso:               
                            `++shyhdmmmohmdhysssyyysssyhhhyohmmmdyssyssyyyhdmNNNNNNNNNNNNNNNNMMNmmmddhhdNmdmhhysyyyossyyhdsssys+:..+++y.              
                            .osydhddmmdyddddddddhyyyhhyhhysohmmmdsssyyyyhmmNNNNNNNNNNNNNNNNMMMMNMmmmNNdmMNmNmdhysoossyhyhhhhyosso:-y/-o+              
                            :yyhddddmNmhhdddddmmmmmdhhyssyyohmmmmoysyhmmNNNNNNNNNNNNNNNNNNMMMMMMMNmmNmdNNmmNdhmdhhsssyyhhhdddhs+oosyo+:s              
                            -dhdmmmmmNmhyddhdmmmmmmNNmmdhyyhhmmmmdhmmNNNNNNNNNNNNNNNNNNNNNNMNMMMMMMmmmmNNNNNNNdmmhdhyyyhhhdhmmdhyyyhhhys`             
                             sddmmNNNNNhhddddmmmmmmmNNmmmmdmhdmdddmNNNNNNNNNNNNNNNNNNNNNNNNNMMMMMMMMNNNNNNNNNNNmdmdmdhhdddhddmdymNdhmdd+:             
                             .mmmNNNNNNmyhhdmmmNmmmmNNNNNNNddhmdhdmNNNNNNNNNNNNNNNNNNNNNNNNNMMMMMMMMMmNNNmNNNNNNNmmmmmmdysyhhdymdhmdddh:-             
                              oysdNNNNNNhhddmmmNmNmNNNNNNNNmdymdhdmNNNNNNNNNNNNNNNNNNNNNNNNNNMMMMMMMMMNNNNNNNNNNNNmdmmmmmmdhddmhshdhdh+:.             
                               :/ohmNNNMmddmmmNNNNmNmNNNNNNmdydmhddNNNNNNNNNNMMNNNNNNNNNNNNNMMMMMMNNNNmmNNNNNNNNNNNNmmmdmmmmmdyyhdhhhs/:.             
                              y+/ommNNNMNdmmmmNNNNNNNNNNNNNNdhhmhddNNNNNNMMNNNNNNNNNNNNNNNMMMMMMMNNNmmmmmNNNNNNNMMNNNNmNNNmmddhmdhddyo+/:             
                             .y++hdNNNNMMNmmmNNNNNNNNMNNNNNNNhyddddNNNNNNNNNNNNNNNNNNNNNMMNNNMMNNNmmmmmddhmNNNNNNNNNNNmdmmmNdmdhmddhyso/.             
                            -ssoodmNNNNMMNNmmNNNNNNNNNNNNNNNNmdhmddNNNNNNmNNNNNNNNNNNMMNNNNNNNNNNNmmmmddddmmNNNNNNNNNNNNNNNNmmmmddhhhh+:`             
                          .syyhsydNNNNNMMNNmdmNNNNNNNNNNNNNNNNmmmmmNNNNNNNNNNNNNNNNMMNNNNNNNNNNNmmmmdddddmmhhhdmmmNNNNNNmmmmmmmdhyyss++-              
                         /hoydmhydmNNNNNNNmmmmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNMMMNNNNNNNNNNNNNmmmmmmmdmmhhhddddddddmmmmmmmmmdhysyyy+/`            
    """)


def print_thanos_banner_after_snap():
    print("""
                                      `.--       
                                    -oyyydh:     
                                   :hyyyydmm:    
                                  .yhysoydmNd`   
                                  +ysoosyddmh/   
                                ./ssso+sddddy/   
                                :oyo+++ydmmdd+    
                                .sy//:ohdmmdhs`                         
                                -ss:--+yddmdyy`    
                                /o+--:+yhdmdsy     
                                +oo++osyhddhhy                                                    
                               -so:--:+yyhdssh.                `-/+o/`                              
                               .oo/---/yyhdhohs             `-/ooooydy:                             
                                /s/---:syyhdssh.          -:+ooooyhdhys///+:`                       
                                .oo----+ysyhhoho      `.-:+s//:oydhsso+::/hdy/`                     
                                 /s::://sssyhysh```.-:+++:/o.:oymdsyo//--:hdhhs`                    
                                 .o//-::osyhhhddyo+//:----:o:ohmNsho/:--.:hdddh-                    
                                 `/++osyhs+/+ohhydo:-.....:sshmNdsy/:-..-:yhhdd+                    
                                 +ysh//ooyo:/ooysydo/:-::/sdhdNMyyo:.....-ohhhhs                    
                                  //sy+yysso/+osyshms+oydmddddmmsso++ooo/:+yhhhy                    
                               -.-oo+ysosssys/+oyyymNNmdddhhhhddNNhyooooshhdhhys                    
                           .../syyyyoos+/+ooss+shddhmmNmdhhhho-.dyo::-.-/syyhmmdo`                  
                         -++--+mMNmddooo+/:/+syhdNNmdhyho/:-`  `dhyo:/syyssydmmmd.                  
                      `..//-+yNMNNmmmy/:...-:/osyNNhssso+:.`    ymhsso/--:+ssshhy/`                 
                    -/o/+oydhdNNmmmmo:-:::-:/+o+ymNmdyyyhsyhs  `shy+:-::-::/+oyhhhs-                
                 `+.:yhshy+--/++ss+:-+so+/.:/+s+smNmmdhysyhmh+`-sy+:-//:::++oyhddddh+               
                 ++/ymyyo///::-.-:::yy+//.``:++ysmNNdhhsydNdyys+ys+/oyyyyhdddmmmNNNdo               
               `:/ohyoss+++o+:os/+:oh+o+/. `-ooshhmNmddhyhNdhddsyso/++syhddhddmmNNmy.               
             `:/sy/--sssyssys+/so/:hd+/++-`.:soydhmNNNmdhmMmNmyssyoo/::/+syydddmNNN/                
             :/++/:--/+yoyy++:o+h+/smyo++/:/ossdyydmNNNddNMMmdsysyyyssso++++osyhddm`                
            .+o++:/--/oysso/:`/osy/oydhooo+++syhysdhmNNNmNNmdhssyys+/osydmdddmmNNms                 
         `../oyy+-:/:/ooso+//-+sod+ooosso+++syyyyysshmNNNmdmdysyyhyhyhhhddddddddmmo                 
        .+++ooos+--+//osssooo+osom++s+//+//+ossyyyoosdNNMdNysyyyhddsosyyhhhhhhddmdms`               
       `ss+:o/oo+.`+o/+sso+++/oshy++osoo+++osoyyyyysyyhmdmmhshydmyoshdhssyyssshhmmmm:               
       `oso-/+sso--oyooso+/+sooo+/oosooyo++ossyyyyyyyyshoNNhshdNyossyhhssyysyyyyddmNo               
       `//:.:+sss+osh+oyoo//+++o++o//++sooososyysyyyyhhhsymNmdNhh+:+ysoyhhhyhhdyshdmm`              
        :/:./yo+ysssyooso+//+oosooo:::+ooyossysssssyoyyoymNNNMmyh:/sosysssss+odhssdNN.              
        `-//+hs+syso+oo++:-:+oyyhyosh+:oyysysysysyyomNdNMMMNNMyy:/++hyosyso+/yhdhyhmm`              
         `-/ody++ssooo+++:.-++osyhymmdo:yyhhhyyyyy+mMMNNNNmNMdh++o+sssysss+/+syyhhdmo               
            :yso/+yss+/:/:.-:+oosshmmdh/sdddddhhhoyMMNNNNNNNNyh+sy/ys++oyys+/oyyyhdy`               
             .os+:oyy/--..``-+sooyodNmdoomhhhhhhh+mMNNNNNNNMhm+oy+ymyyhdsy+-./yyydh.                
              -os/hhs/:-..`.-/+yosyhNh+/oy++dhhhdshMMNNNNNMNhhoyd+mmdddhhy/../shhh:                 
               -ooomy+/-..`..-:shsdydmssyyo+dhdddddmNNNNNNMdmsydhsmmmdmddy+::oyhd/                  
                :o+hhy:-.....-:+hyddhMNdmNdsyNddmmmNmmNNNMMhdshddhNmmmdmmds//shdo                   
                `/soyho--..----/hhNhhMNmhysyhmNmNNNdNmdNMMMdhyddmmNNNNmmmmdyydmy`                   
                 .soohdo:-..---/ddNyhMhoosdhddNNNNNNNNNmmNNmhhdmmNNNMNNmdddddmh.                    
                  :+hNddhs/://ohdNdhNmoymNMmddNNNNNNNNNMNMNmmmNNNNNmNNNmmmNmdh.                     
                   :oshydyyyhddmmdymMmNNmmmhmNNNmmmmNNNmdydNNNNNNNNNmmmmNNNdh-                      
                    :+sooosydhmhhhNMdyyhmNhdMmmNNNNNmdyo+dMNNNNNNNNNmNNNNNmy.                       
                     -+hmhhhhhddNNmhyNdysyNMNNNNNmdhso/sNmMddNNNNNNNNMMMNmo`                        
                      :ohddsoymNmmNNhMNhNmmmmhhhyyyo/omNhodNhhNNNNNNMNNmh:                          
                       /yyosddhNdNMNmmddhddhyosoosoodNdys+hmmhhNNmddddyhhy/                         
                        /hhhyhhmMMNmmd+s://+ooososmNdyssssymNmdhNNNdhhyymdd-                        
                         /yhyooymmdmms-:s/++so+sdmmhsysso+ymmmNhymmmdhdmmmd.                        
                         `syo+/hNdsyy::-so//ohmdyosdddys+/odmmmNmmmmmmmmmmy+                        
                         `+s+/yMmhshs.+/syddhyhdhyyssydh:+ommmmmmNmmdyyyhddh:                       
                         `/o/yMNhdmhhymmNmdhhsosdmmhs++//ydNdmmmmmmmddhhdmmhs                       
                          `/oNNhdmhhddNdddhhyydhyyydh+/sdNmddmmmmNNNNNmmmNNmh                       
                          -yhyhhmmdhhdNyoymmdyyhhhs//ohmmmdddmdmmmmmmmmmmmNmd-                      
                          ydyddmhos+osyhho+ymmhys+/odmdmmmmmmmmmmmmmmmmdddmmmy                      
                         /myNyhmys+::ymmmhysommh+omNmdmmNmNNNmmmmmmmmmmdddmNNm/                     
                        .hymdsmm+s+/sdhdhymhysmmmyymmmmmmmmmmdddmddddddddmNNMNd`                    
                        -+dyyhNhsyssdyyyymshhysmmmsodddddddhhhhyyhhdddmNNNNNNNm+                    
                         +dyyhyoydshdddomsosmyyomdmy+hhhyyhysoshddhmNNNmNNNNNmmd`                   
                        .osdosy/syy/mmoddsssoddoshyhh/osso++ydddhdhhNmmmNNNNNmdd/                   
                        /odyo+y/ydo/osymdsshdmhhsosymd+//+hddhdddmhymmNNNmmNNmddy                   
                       .oyds+ossyoss+oNmdssohdmhhdmmmNmydmhhhhhddmhhdNNNmmNmNmmmm-                  
                       +smho+smhyyysysNmmyysyyymmmdhhhddhhyhyyhdddddhNNNNNNmNmdmms                  
                      .ohhs//hmyhyssysNmdhhshyyhhhhhyyhhhhhyyhddddmdhmNmdddmNNmdmm`                 
                      :sdsyyyNdsyy+ohyNNmhhohhhhhhyyyyyhhyyhhhddddmhhmNmhmmmNNmdmm/                 
                     `+ydy+shNhyshohmyNNmdhoyddhhhhhhhyhyhhdhddddmddddNNhhddmNmddNy                 
                     -ydsyhomNydhosdmhNNmdmsyddhhhdhhhdddhhhhhhddddmmhNNdmNNmNNdmmm`                
                     oydy++yNmhhhdydmhNNmddysddhydddddddddhhhhhdddhdmhNNmhhdddNmdmN-                
                    .shshosyNmNNmssdmyNNmmmdshdhhhdhdddddddhhddhhhhdmddNmhmNmmNNNmN+                
                    /odhsdysNmy+osymmyNNmmNmsydddhhddmddddddddddhyhdmmhNmdhhmdNNmmNs                
    """)