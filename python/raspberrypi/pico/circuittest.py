from machine import Pin
import segmentdisplays

def main():
    segdisp = segmentdisplays.segdisplays()
    try:
        print("circuit test...")
        segmentdisplays.showbacknumberOneSegonly(segdisp, 0x01 << 7)
        segmentdisplays.showbackfloatOneSegonly(segdisp, 0x01 << 7)
        segmentdisplays.showforwardfloatOneSegonly(segdisp, 0x01 << 7)
        segmentdisplays.showforwardnumberOneSegonly(segdisp, 0x01 << 7)

        segmentdisplays.showbacknumber(segdisp)
        segmentdisplays.showbackfloat(segdisp)
        segmentdisplays.showforwardfloat(segdisp)
        segmentdisplays.showforwardnumber(segdisp)

        segmentdisplays.showbacknumberOneSegonly(segdisp, 0x01 << 6)
        segmentdisplays.showbackfloatOneSegonly(segdisp, 0x01 << 6)
        segmentdisplays.showforwardfloatOneSegonly(segdisp, 0x01 << 6)
        segmentdisplays.showforwardnumberOneSegonly(segdisp, 0x01 << 6)
    finally:
        print("test finished")

if __name__ == '__main__':
	main()