"use client";

import { observer } from "mobx-react";
import { LucideIcon, Users } from "lucide-react";
// youtrack ui
import { Avatar, AvatarGroup } from "@youtrack/ui";
// helpers
import { getFileURL } from "@/helpers/file.helper";
// hooks
import { useMember } from "@/hooks/store";

type AvatarProps = {
  showTooltip: boolean;
  userIds: string | string[] | null;
  icon?: LucideIcon;
};

export const ButtonAvatars: React.FC<AvatarProps> = observer((props) => {
  const { showTooltip, userIds, icon: Icon } = props;
  // store hooks
  const { getUserDetails } = useMember();

  if (Array.isArray(userIds)) {
    if (userIds.length > 0)
      return (
        <AvatarGroup size="md" showTooltip={!showTooltip}>
          {userIds.map((userId) => {
            const userDetails = getUserDetails(userId);

            if (!userDetails) return;
            return <Avatar key={userId} src={getFileURL(userDetails.avatar_url)} name={userDetails.display_name} />;
          })}
        </AvatarGroup>
      );
  } else {
    if (userIds) {
      const userDetails = getUserDetails(userIds);
      return (
        <Avatar
          src={getFileURL(userDetails?.avatar_url ?? "")}
          name={userDetails?.display_name}
          size="md"
          showTooltip={!showTooltip}
        />
      );
    }
  }

  return Icon ? <Icon className="h-3 w-3 flex-shrink-0" /> : <Users className="h-3 w-3 mx-[4px] flex-shrink-0" />;
});
